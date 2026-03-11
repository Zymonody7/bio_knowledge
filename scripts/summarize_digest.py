#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV = ROOT / "outputs" / "papers.csv"
DEFAULT_MD = ROOT / "outputs" / "daily_digest.md"
RAW_DIR = ROOT / "data" / "raw"


CATEGORY_TITLES = {
    "foundation_model": "Foundation Model / Agent",
    "dataset": "数据集 / Benchmark",
    "methods": "方法创新",
    "clinical_application": "产品应用 / 监测落地",
    "general": "其他",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a Chinese daily digest from papers.csv.")
    parser.add_argument("--input", default=str(DEFAULT_CSV))
    parser.add_argument("--output", default=str(DEFAULT_MD))
    return parser.parse_args()


def load_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_fetch_statuses() -> list[dict]:
    statuses: list[dict] = []
    for path in sorted(RAW_DIR.glob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for item in payload.get("source_statuses", []):
            statuses.append(item)
    return statuses


def to_float(value: str) -> float:
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


def summarize_error(error: str, limit: int = 140) -> str:
    compact = " ".join((error or "").split())
    if " for url: " in compact:
        compact = compact.split(" for url: ", 1)[0]
    if len(compact) <= limit:
        return compact
    return compact[:limit].rstrip() + "..."


def render_section(title: str, rows: list[dict]) -> list[str]:
    lines = [f"## {title}", ""]
    if not rows:
        lines.append("今天这一档没有命中论文。")
        lines.append("")
        return lines

    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[row.get("category", "general")].append(row)

    for category in ("foundation_model", "dataset", "methods", "clinical_application", "general"):
        group_rows = grouped.get(category, [])
        if not group_rows:
            continue
        lines.append(f"### {CATEGORY_TITLES[category]}")
        lines.append("")
        for row in group_rows:
            matched_topics = row.get("matched_topics", "").replace(";", ", ")
            abstract_zh = (row.get("abstract_zh") or "").strip()
            abstract_preview = abstract_zh or row.get("abstract", "")
            lines.append(f"- [{row['title']}]({row['url']})")
            lines.append(f"  来源：{row['source']} | 日期：{row['date'][:10]} | 相关度：{row['relevance_score']} | 新颖度：{row['novelty_score']}")
            lines.append(f"  匹配主题：{matched_topics or '未命中具体主题'}")
            lines.append(f"  中文摘要：{abstract_preview[:220]}{'...' if len(abstract_preview) > 220 else ''}")
            lines.append(f"  为什么值得看：{row['why_it_matters']}")
            lines.append("")
    return lines


def main() -> int:
    args = parse_args()
    rows = load_rows(Path(args.input))
    buckets = {"最值得看": [], "可追踪": [], "低优先级": []}
    for row in rows:
        score = to_float(row.get("relevance_score")) * 0.65 + to_float(row.get("novelty_score")) * 0.35
        if score >= 7.0:
            buckets["最值得看"].append(row)
        elif score >= 4.5:
            buckets["可追踪"].append(row)
        else:
            buckets["低优先级"].append(row)

    today = datetime.now().strftime("%Y-%m-%d")
    fetch_statuses = load_fetch_statuses()
    success_statuses = [status for status in fetch_statuses if status.get("success")]
    failed_statuses = [status for status in fetch_statuses if not status.get("success")]
    total_hits = sum(int(status.get("count", 0) or 0) for status in success_statuses)
    lines = [
        f"# 每日论文监控日报 ({today})",
        "",
        "本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。",
        "",
        f"今日共整理 {len(rows)} 篇新论文。",
        "",
    ]

    if fetch_statuses and not rows and success_statuses and total_hits == 0:
        lines.extend(
            [
                "## 今日说明",
                "",
                "本次抓取成功执行，但在当前检索窗口内没有命中新增候选论文。",
                "这表示这次是“成功抓取但结果为 0”，不是网络失败；知识库与站点仍会基于历史累计论文重建。",
                "",
            ]
        )

    if fetch_statuses and not rows and failed_statuses and not success_statuses:
        lines.extend(
            [
                "## 今日说明",
                "",
                "本次抓取阶段全部失败，当前结果主要来自历史缓存或累计知识库，不应解读为当天没有新论文。",
                "",
            ]
        )

    if fetch_statuses:
        lines.append("## 抓取状态")
        lines.append("")
        for status in fetch_statuses:
            outcome = "成功" if status.get("success") else "失败"
            error = status.get("error", "")
            count = status.get("count", 0)
            if error:
                lines.append(
                    f"- {status.get('source', 'unknown')}：{outcome}，命中 {count} 篇，错误：{summarize_error(error)}"
                )
            else:
                lines.append(f"- {status.get('source', 'unknown')}：{outcome}，命中 {count} 篇")
        if any(not status.get("success") for status in fetch_statuses):
            lines.append("")
            lines.append("注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。")
        lines.append("")

    for bucket_name in ("最值得看", "可追踪", "低优先级"):
        lines.extend(render_section(bucket_name, buckets[bucket_name]))

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    print(f"Wrote digest to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
