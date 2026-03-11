#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import time
from pathlib import Path

import requests

from rag_config import DEFAULT_CONFIG, load_rag_config


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "outputs" / "papers.csv"
DEFAULT_CACHE = ROOT / "data" / "processed" / "paper_enrichment.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Enrich papers.csv with Chinese abstract translations and detailed AI analysis.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--cache", default=str(DEFAULT_CACHE))
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--limit", type=int, default=12)
    return parser.parse_args()


def load_csv_rows(path: Path) -> tuple[list[str], list[dict]]:
    if not path.exists():
        return [], []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv_rows(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalize_text(text: str) -> str:
    return " ".join((text or "").lower().split())


def normalize_doi(value: str) -> str:
    doi = (value or "").strip().lower()
    if doi.startswith("10.1101/10."):
        return doi.split("/", 1)[1]
    return doi


def canonical_id(row: dict) -> str:
    doi_value = normalize_doi(row.get("doi", ""))
    if doi_value:
        return f"doi:{doi_value}"
    for key in ("arxiv_id", "pubmed_id"):
        value = (row.get(key) or "").strip().lower()
        if value:
            return f"{key}:{value}"
    return f"title:{normalize_text(row.get('title', ''))}"


def content_hash(row: dict) -> str:
    payload = {
        "title": row.get("title", ""),
        "source": row.get("source", ""),
        "date": row.get("date", ""),
        "url": row.get("url", ""),
        "abstract": row.get("abstract", ""),
        "matched_topics": row.get("matched_topics", ""),
        "relevance_score": row.get("relevance_score", ""),
        "novelty_score": row.get("novelty_score", ""),
        "why_it_matters": row.get("why_it_matters", ""),
        "category": row.get("category", ""),
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def is_placeholder_analysis(text: str) -> bool:
    compact = (text or "").strip()
    return "当前为规则型离线解读" in compact or "当前没有使用远程 LLM 生成详细解读" in compact


def extract_json_block(text: str) -> dict:
    content = (text or "").strip()
    if content.startswith("```"):
        lines = content.splitlines()
        if len(lines) >= 3:
            content = "\n".join(lines[1:-1]).strip()
    start = content.find("{")
    end = content.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object found in model response")
    return json.loads(content[start:end + 1])


def build_messages(row: dict) -> list[dict]:
    return [
        {
            "role": "system",
            "content": (
                "你是病原生信、蛋白质组学、基因组学、临床微生物学与 AI/LLM/Agent 交叉领域的中文研究助手。"
                "你的任务是根据给定论文元数据与英文摘要，生成高质量中文摘要翻译和详细 AI 解读。"
                "只根据提供内容输出，不要编造不存在的实验细节。禁止使用空话、套话、泛化结论。输出必须是 JSON。"
            ),
        },
        {
            "role": "user",
            "content": (
                "请严格输出 JSON，对象包含 `abstract_zh` 和 `analysis_zh` 两个字段。\n"
                "`abstract_zh`：把英文摘要忠实翻译成自然中文，优先保留研究对象、数据、方法、结果、结论，180-320 字。不要写成泛泛介绍。\n"
                "`analysis_zh`：使用 markdown，按以下小节输出：\n"
                "## 核心内容\n## 为什么相关\n## 新颖度判断\n## 方法与证据\n## 应用价值\n## 局限与风险\n"
                "要求：\n"
                "- 用中文，具体，不要空话。\n"
                "- 结合论文来源、主题、相关度、新颖度来判断。\n"
                "- 每一节都要引用摘要里已经出现的具体信息，例如模型名、任务、数据规模、实验对象、指标或结论；如果摘要没有写，就明确说“摘要未说明”。\n"
                "- 如果只是弱 AI 交叉，要明确指出，不要硬说成强相关。\n"
                "- 不要重复标题，不要只改写 why_it_matters，不要输出“值得关注”“可以先判断”这类空泛句。\n\n"
                f"标题：{row.get('title', '')}\n"
                f"来源：{row.get('source', '')}\n"
                f"日期：{row.get('date', '')}\n"
                f"分类：{row.get('category', '')}\n"
                f"匹配主题：{row.get('matched_topics', '')}\n"
                f"相关度：{row.get('relevance_score', '')}\n"
                f"新颖度：{row.get('novelty_score', '')}\n"
                f"为什么值得看：{row.get('why_it_matters', '')}\n"
                f"英文摘要：{row.get('abstract', '')}\n"
            ),
        },
    ]


def enrich_with_remote(row: dict, config: dict) -> dict:
    chat_cfg = config.get("chat", {})
    if chat_cfg.get("provider") != "openai_compatible":
        raise ValueError("Only openai_compatible chat provider is supported for enrichment")

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required for remote enrichment")

    response = requests.post(
        f"{chat_cfg['base_url'].rstrip('/')}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": chat_cfg["model"],
            "temperature": float(chat_cfg.get("temperature", 0.2)),
            "messages": build_messages(row),
        },
        timeout=180,
    )
    response.raise_for_status()
    payload = response.json()
    message = payload["choices"][0]["message"]["content"]
    parsed = extract_json_block(message)
    abstract_zh = (parsed.get("abstract_zh") or "").strip()
    analysis_zh = (parsed.get("analysis_zh") or "").strip()
    if not abstract_zh or not analysis_zh:
        raise ValueError("Model response missing abstract_zh or analysis_zh")
    return {
        "abstract_zh": abstract_zh,
        "analysis_zh": analysis_zh,
    }


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    cache_path = Path(args.cache)
    fieldnames, rows = load_csv_rows(input_path)
    if not rows:
        print(f"No rows to enrich in {input_path}")
        return 0

    for field in ("abstract_zh", "analysis_zh"):
        if field not in fieldnames:
            fieldnames.append(field)

    cache = load_json(cache_path)
    cache_records = cache.setdefault("papers", {})
    config = load_rag_config(Path(args.config))
    can_use_remote = bool(os.getenv("OPENAI_API_KEY", "").strip() and config.get("chat", {}).get("base_url") and config.get("chat", {}).get("model"))
    updated = 0
    reused = 0

    rows_to_enrich = sorted(
        rows,
        key=lambda row: (
            -float(row.get("relevance_score") or 0),
            -float(row.get("novelty_score") or 0),
            row.get("date", ""),
        ),
        reverse=False,
    )
    rows_to_enrich = list(reversed(rows_to_enrich))[: max(1, args.limit)]
    target_ids = {canonical_id(row) for row in rows_to_enrich}

    for row in rows:
        paper_id = canonical_id(row)
        digest = content_hash(row)
        cached = cache_records.get(paper_id, {})
        if (
            cached.get("content_hash") == digest
            and cached.get("abstract_zh")
            and cached.get("analysis_zh")
            and not is_placeholder_analysis(cached.get("analysis_zh", ""))
        ):
            row["abstract_zh"] = cached["abstract_zh"]
            row["analysis_zh"] = cached["analysis_zh"]
            reused += 1
            continue

        if paper_id not in target_ids:
            row["abstract_zh"] = cached.get("abstract_zh", row.get("abstract_zh", ""))
            row["analysis_zh"] = cached.get("analysis_zh", row.get("analysis_zh", ""))
            continue

        if can_use_remote:
            try:
                enriched = enrich_with_remote(row, config)
            except Exception as exc:
                print(f"Remote enrichment failed for {paper_id}: {exc}")
                enriched = None
            else:
                time.sleep(0.8)
        else:
            enriched = None

        if enriched:
            row["abstract_zh"] = enriched["abstract_zh"]
            row["analysis_zh"] = enriched["analysis_zh"]
            cache_records[paper_id] = {
                "paper_id": paper_id,
                "content_hash": digest,
                "title": row.get("title", ""),
                "abstract_zh": enriched["abstract_zh"],
                "analysis_zh": enriched["analysis_zh"],
                "mode": "remote",
            }
            updated += 1
        else:
            row["abstract_zh"] = ""
            row["analysis_zh"] = ""

    cache["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    write_csv_rows(input_path, fieldnames, rows)
    save_json(cache_path, cache)
    mode = "remote" if can_use_remote else "disabled"
    print(f"Enriched papers using {mode} mode")
    print(f"Updated: {updated}")
    print(f"Reused: {reused}")
    print(f"CSV: {input_path}")
    print(f"Cache: {cache_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
