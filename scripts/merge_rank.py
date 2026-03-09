#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml
from dateutil import parser as date_parser


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
STATE_PATH = ROOT / "data" / "state.json"
OUTPUT_CSV = ROOT / "outputs" / "papers.csv"
DEFAULT_TOPICS = ROOT / "config" / "topics.yaml"


CSV_FIELDS = [
    "title",
    "source",
    "date",
    "url",
    "abstract",
    "matched_topics",
    "relevance_score",
    "novelty_score",
    "why_it_matters",
    "category",
    "doi",
    "arxiv_id",
    "pubmed_id",
]


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def normalize_text(text: str) -> str:
    return " ".join(text.lower().split())


def significant_tokens(keyword: str) -> list[str]:
    stopwords = {"for", "and", "the", "of", "in", "to", "ai"}
    tokens = []
    for raw in keyword.replace("/", " ").replace("-", " ").split():
        token = raw.strip().lower()
        if len(token) >= 4 and token not in stopwords:
            tokens.append(token)
    return tokens[:4]


AI_TOKENS = {
    "ai",
    "llm",
    "rag",
    "transformer",
    "multimodal",
    "copilot",
    "generative",
    "language",
}


def keyword_matches(haystack: str, keyword: str, group_name: str = "") -> bool:
    lowered = keyword.lower()
    if lowered in haystack:
        return True
    tokens = significant_tokens(keyword)
    if len(tokens) < 2:
        return False
    if group_name in {"foundation_model_agent", "data_fair_training"}:
        if not any(token in AI_TOKENS for token in tokens):
            return False
        required = [token for token in tokens if token in AI_TOKENS][:2]
        optional = [token for token in tokens if token not in AI_TOKENS][:2]
        return all(token in haystack for token in required) and any(token in haystack for token in optional or required)
    return all(token in haystack for token in tokens)


def count_term_hits(haystack: str, terms: list[str]) -> int:
    hits = 0
    for term in terms:
        normalized = (term or "").strip().lower()
        if not normalized:
            continue
        pattern = r"\b" + re.escape(normalized).replace(r"\ ", r"\s+") + r"\b"
        if re.search(pattern, haystack):
            hits += 1
    return hits


def canonical_id(paper: dict) -> str:
    for key in ("doi", "arxiv_id", "pubmed_id"):
        value = (paper.get(key) or "").strip().lower()
        if value:
            return f"{key}:{value}"
    return f"title:{normalize_text(paper.get('title', ''))}"


def load_raw_papers() -> list[dict]:
    papers = []
    for path in sorted(RAW_DIR.glob("*.json")):
        payload = load_json(path)
        papers.extend(payload.get("papers", []))
    return papers


def match_topics(paper: dict, topics: dict) -> tuple[list[str], float]:
    haystack = normalize_text(" ".join([paper.get("title", ""), paper.get("abstract", "")]))
    matched = []
    score = 0.0
    for group in topics.get("topic_groups", []):
        group_matched = False
        for keyword in group.get("keywords", []):
            if keyword_matches(haystack, keyword, group.get("name", "")):
                group_matched = True
                score += group.get("priority", 0.5)
        if group_matched:
            matched.append(group["name"])
    return matched, min(score, 10.0)


def collect_focus_phrases(topics: dict) -> list[str]:
    phrases = []
    seen = set()
    topic_groups = {group.get("name"): group for group in topics.get("topic_groups", [])}
    for name in topics.get("query_groups", []):
        group = topic_groups.get(name, {})
        for keyword in group.get("keywords", []):
            lowered = keyword.strip().lower()
            if lowered and lowered not in seen:
                seen.add(lowered)
                phrases.append(lowered)
    for keyword in topics.get("query_keywords", []):
        lowered = keyword.strip().lower()
        if lowered and lowered not in seen:
            seen.add(lowered)
            phrases.append(lowered)
    return phrases


def compute_focus_scores(paper: dict, topics: dict) -> tuple[int, int, int, int]:
    haystack = normalize_text(" ".join([paper.get("title", ""), paper.get("abstract", "")]))
    ranking = topics.get("ranking", {})
    ai_score = count_term_hits(haystack, ranking.get("ai_anchor_terms", []))
    domain_score = count_term_hits(haystack, ranking.get("domain_anchor_terms", []))
    exact_focus_score = count_term_hits(haystack, collect_focus_phrases(topics))
    negative_score = count_term_hits(haystack, ranking.get("negative_anchor_terms", []))
    return ai_score, domain_score, exact_focus_score, negative_score


def should_keep_paper(category: str, matched_topics: list[str], ai_score: int, exact_focus_score: int, negative_score: int, topics: dict) -> bool:
    ranking = topics.get("ranking", {})
    if negative_score > 0:
        return False
    if ai_score > 0:
        return True
    if exact_focus_score > 0:
        return True
    keep_categories = set(ranking.get("keep_without_ai_categories", []))
    return category in keep_categories


def infer_category(paper: dict, topics: dict) -> str:
    haystack = normalize_text(" ".join([paper.get("title", ""), paper.get("abstract", "")]))
    best_category = "general"
    best_hits = 0
    for category, keywords in topics.get("category_keywords", {}).items():
        hits = count_term_hits(haystack, keywords)
        if hits > best_hits:
            best_hits = hits
            best_category = category
    return best_category


def compute_novelty(paper: dict, seen_ids: set[str]) -> float:
    score = 5.0 if canonical_id(paper) not in seen_ids else 0.0
    date_value = paper.get("date", "")
    try:
        dt = date_parser.parse(date_value).astimezone(timezone.utc)
        age_hours = max(0.0, (datetime.now(timezone.utc) - dt).total_seconds() / 3600.0)
        score += max(0.0, 4.0 - age_hours / 6.0)
    except (ValueError, TypeError):
        pass

    haystack = normalize_text(" ".join([paper.get("title", ""), paper.get("abstract", "")]))
    innovation_terms = ["foundation model", "benchmark", "dataset", "long-read", "nanopore", "unknown pathogen"]
    score += min(2.0, sum(0.5 for term in innovation_terms if term in haystack))
    return round(min(score, 10.0), 2)


def generate_why_it_matters(paper: dict, matched_topics: list[str], category: str) -> str:
    title = paper.get("title", "")
    source = paper.get("source", "")
    if "foundation_model" == category:
        return f"这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。"
    if "dataset" == category:
        return f"这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。"
    if "methods" == category:
        return f"这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。"
    if "clinical_application" == category:
        return f"这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。"
    if matched_topics:
        return f"{source} 上的新论文与 {', '.join(matched_topics)} 相关，可用于补充你当前的病原检测与模型监控视角。"
    return f"{title[:40]} 与你的主题有弱匹配，暂时保留作低优先级跟踪。"


def rank_bucket(relevance: float, novelty: float) -> str:
    combined = relevance * 0.65 + novelty * 0.35
    if combined >= 7.0:
        return "最值得看"
    if combined >= 4.5:
        return "可追踪"
    return "低优先级"


def deduplicate(papers: list[dict]) -> list[dict]:
    deduped: dict[str, dict] = {}
    for paper in papers:
        key = canonical_id(paper)
        existing = deduped.get(key)
        if existing is None:
            deduped[key] = paper
            continue
        existing_abstract = len(existing.get("abstract", ""))
        current_abstract = len(paper.get("abstract", ""))
        if current_abstract > existing_abstract:
            deduped[key] = paper
    return list(deduped.values())


def prune_seen(seen: dict[str, str], keep_days: int = 180) -> dict[str, str]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=keep_days)
    pruned = {}
    for key, value in seen.items():
        try:
            if date_parser.parse(value).astimezone(timezone.utc) >= cutoff:
                pruned[key] = value
        except (ValueError, TypeError):
            continue
    return pruned


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Merge raw papers, deduplicate, score, and write CSV/state.")
    parser.add_argument("--topics", default=str(DEFAULT_TOPICS))
    parser.add_argument("--state", default=str(STATE_PATH))
    parser.add_argument("--output", default=str(OUTPUT_CSV))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    topics = load_yaml(Path(args.topics))
    state_path = Path(args.state)
    state = load_json(state_path)
    seen = prune_seen(state.get("seen", {}))
    raw_papers = deduplicate(load_raw_papers())

    ranked = []
    for paper in raw_papers:
        matched_topics, relevance = match_topics(paper, topics)
        category = infer_category(paper, topics)
        ai_score, domain_score, exact_focus_score, negative_score = compute_focus_scores(paper, topics)
        if not should_keep_paper(category, matched_topics, ai_score, exact_focus_score, negative_score, topics):
            continue
        if ai_score == 0:
            relevance *= 0.4
        else:
            relevance += min(2.5, ai_score * 0.7)
        relevance += min(2.0, exact_focus_score * 0.9)
        if ai_score > 0 and domain_score > 0:
            relevance += 1.0
        novelty = compute_novelty(paper, set(seen))
        if ai_score > 0:
            novelty = round(min(10.0, novelty + min(1.2, ai_score * 0.25)), 2)
        ranked.append(
            {
                **paper,
                "matched_topics": matched_topics,
                "relevance_score": round(min(relevance, 10.0), 2),
                "novelty_score": novelty,
                "why_it_matters": generate_why_it_matters(paper, matched_topics, category),
                "category": category,
                "bucket": rank_bucket(relevance, novelty),
            }
        )

    ranked.sort(
        key=lambda item: (
            {"最值得看": 0, "可追踪": 1, "低优先级": 2}[item["bucket"]],
            -item["relevance_score"],
            -item["novelty_score"],
            item["date"],
        )
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for paper in ranked:
            row = {field: paper.get(field, "") for field in CSV_FIELDS}
            row["matched_topics"] = ";".join(paper.get("matched_topics", []))
            writer.writerow(row)

    timestamp = datetime.now(timezone.utc).isoformat()
    for paper in ranked:
        seen[canonical_id(paper)] = timestamp
    state_path.parent.mkdir(parents=True, exist_ok=True)
    with state_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "updated_at": timestamp,
                "seen": seen,
                "latest_run_count": len(ranked),
            },
            handle,
            ensure_ascii=False,
            indent=2,
        )

    category_summary: dict[str, int] = defaultdict(int)
    for paper in ranked:
        category_summary[paper["category"]] += 1
    print(f"Wrote {len(ranked)} papers to {output_path}")
    print("Category summary:", json.dumps(category_summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
