#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PAPERS = ROOT / "outputs" / "papers.csv"
DEFAULT_KB_JSON = ROOT / "data" / "processed" / "knowledge_base.json"
DEFAULT_KB_MD = ROOT / "outputs" / "knowledge_base.md"
DEFAULT_STATS_MD = ROOT / "outputs" / "knowledge_base_stats.md"

SCHEMA_VERSION = "1.0"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a cumulative local knowledge base from papers.csv.")
    parser.add_argument("--input", default=str(DEFAULT_PAPERS))
    parser.add_argument("--json-output", default=str(DEFAULT_KB_JSON))
    parser.add_argument("--md-output", default=str(DEFAULT_KB_MD))
    parser.add_argument("--stats-output", default=str(DEFAULT_STATS_MD))
    return parser.parse_args()


def load_csv_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def normalize_text(text: str) -> str:
    return " ".join(text.lower().split())


def canonical_id(row: dict) -> str:
    for key in ("doi", "arxiv_id", "pubmed_id"):
        value = (row.get(key) or "").strip().lower()
        if value:
            return f"{key}:{value}"
    return f"title:{normalize_text(row.get('title', ''))}"


def parse_topics(value: str) -> list[str]:
    return [item for item in (value or "").split(";") if item]


def parse_float(value: str | float | None) -> float:
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return 0.0


def parse_date(value: str) -> str:
    return value or ""


def stable_payload_hash(record: dict) -> str:
    payload = {
        "title": record.get("title", ""),
        "abstract": record.get("abstract", ""),
        "matched_topics": record.get("matched_topics", []),
        "category": record.get("category", ""),
        "why_it_matters": record.get("why_it_matters", ""),
        "source": record.get("source", ""),
        "date": record.get("date", ""),
        "url": record.get("url", ""),
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def build_record(row: dict, paper_id: str, now: str) -> dict:
    title = row.get("title", "")
    abstract = row.get("abstract", "")
    topics = parse_topics(row.get("matched_topics", ""))
    date_value = parse_date(row.get("date", ""))
    return {
        "paper_id": paper_id,
        "title": title,
        "source": row.get("source", ""),
        "date": date_value,
        "year": date_value[:4] if len(date_value) >= 4 else "",
        "url": row.get("url", ""),
        "abstract": abstract,
        "abstract_short": abstract[:400],
        "matched_topics": topics,
        "topic_count": len(topics),
        "relevance_score": parse_float(row.get("relevance_score")),
        "novelty_score": parse_float(row.get("novelty_score")),
        "importance_score": round(parse_float(row.get("relevance_score")) * 0.65 + parse_float(row.get("novelty_score")) * 0.35, 3),
        "why_it_matters": row.get("why_it_matters", ""),
        "category": row.get("category", "general"),
        "doi": row.get("doi", ""),
        "arxiv_id": row.get("arxiv_id", ""),
        "pubmed_id": row.get("pubmed_id", ""),
        "content_hash": "",
        "first_seen_at": now,
        "last_seen_at": now,
        "times_seen": 1,
        "notes": [],
        "status": "active",
    }


def sort_records(records: list[dict]) -> list[dict]:
    return sorted(
        records,
        key=lambda item: (
            -float(item.get("importance_score", 0)),
            -float(item.get("relevance_score", 0)),
            item.get("date", ""),
            item.get("title", ""),
        ),
    )


def summarize_records(records: list[dict], last_run_count: int) -> dict:
    by_source = Counter(record.get("source", "") for record in records if record.get("source"))
    by_category = Counter(record.get("category", "general") for record in records)
    by_topic = Counter(topic for record in records for topic in record.get("matched_topics", []))
    by_year = Counter(record.get("year", "") for record in records if record.get("year"))

    return {
        "total_papers": len(records),
        "last_run_count": last_run_count,
        "sources": dict(sorted(by_source.items())),
        "categories": dict(sorted(by_category.items())),
        "topics": dict(sorted(by_topic.items())),
        "years": dict(sorted(by_year.items())),
    }


def build_indexes(records: list[dict]) -> dict:
    indexes = {
        "by_source": defaultdict(list),
        "by_category": defaultdict(list),
        "by_topic": defaultdict(list),
        "by_year": defaultdict(list),
    }

    for record in records:
        paper_id = record["paper_id"]
        if record.get("source"):
            indexes["by_source"][record["source"]].append(paper_id)
        indexes["by_category"][record.get("category", "general")].append(paper_id)
        if record.get("year"):
            indexes["by_year"][record["year"]].append(paper_id)
        for topic in record.get("matched_topics", []):
            indexes["by_topic"][topic].append(paper_id)

    return {
        name: {key: sorted(value) for key, value in sorted(groups.items())}
        for name, groups in indexes.items()
    }


def render_markdown(records: list[dict], summary: dict) -> str:
    category_groups: dict[str, list[dict]] = defaultdict(list)
    topic_groups: dict[str, list[dict]] = defaultdict(list)

    for record in records:
        category_groups[record["category"]].append(record)
        for topic in record["matched_topics"]:
            topic_groups[topic].append(record)

    top_topics = sorted(summary["topics"].items(), key=lambda item: (-item[1], item[0]))[:10]
    lines = [
        "# 论文知识库",
        "",
        f"最近更新：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"累计论文数：{summary['total_papers']}",
        f"最近一次新增：{summary['last_run_count']}",
        "",
        "## 概览",
        "",
        f"- 来源分布：{', '.join(f'{key}={value}' for key, value in summary['sources'].items()) or '无'}",
        f"- 类别分布：{', '.join(f'{key}={value}' for key, value in summary['categories'].items()) or '无'}",
        f"- 热门主题：{', '.join(f'{key}={value}' for key, value in top_topics) or '无'}",
        "",
        "## 按类别索引",
        "",
    ]

    for category in sorted(category_groups):
        rows = sort_records(category_groups[category])
        lines.append(f"### {category}")
        lines.append("")
        for row in rows:
            topics = ", ".join(row["matched_topics"]) or "未命中主题"
            lines.append(f"- [{row['title']}]({row['url']})")
            lines.append(f"  来源：{row['source']} | 日期：{row['date'][:10]} | 主题：{topics}")
            lines.append(f"  相关度：{row['relevance_score']} | 新颖度：{row['novelty_score']} | 综合：{row['importance_score']}")
            lines.append(f"  说明：{row['why_it_matters']}")
            lines.append("")

    lines.append("## 按主题索引")
    lines.append("")
    for topic in sorted(topic_groups):
        lines.append(f"### {topic}")
        lines.append("")
        for row in sort_records(topic_groups[topic]):
            lines.append(f"- [{row['title']}]({row['url']}) | {row['source']} | {row['date'][:10]} | score={row['importance_score']}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def render_stats_markdown(summary: dict, indexes: dict) -> str:
    lines = [
        "# 知识库统计",
        "",
        f"更新时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"- 累计论文：{summary['total_papers']}",
        f"- 最近一次新增：{summary['last_run_count']}",
        f"- 来源数：{len(summary['sources'])}",
        f"- 主题数：{len(summary['topics'])}",
        "",
        "## 来源统计",
        "",
    ]

    for source, count in sorted(summary["sources"].items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {source}: {count}")

    lines.extend(["", "## 类别统计", ""])
    for category, count in sorted(summary["categories"].items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {category}: {count}")

    lines.extend(["", "## 主题统计", ""])
    for topic, count in sorted(summary["topics"].items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {topic}: {count}")

    lines.extend(["", "## 索引键", ""])
    for index_name, groups in indexes.items():
        lines.append(f"- {index_name}: {len(groups)}")

    return "\n".join(lines).strip() + "\n"


def main() -> int:
    args = parse_args()
    rows = load_csv_rows(Path(args.input))
    kb_path = Path(args.json_output)
    md_path = Path(args.md_output)
    stats_path = Path(args.stats_output)
    existing_kb = load_json(kb_path)
    existing_papers = existing_kb.get("papers", {})
    state_path = ROOT / "data" / "state.json"
    state = load_json(state_path)
    last_run_count = int(state.get("latest_run_count", len(rows)) or 0)
    now = datetime.now(timezone.utc).isoformat()

    papers: dict[str, dict] = {}
    for paper_id, record in existing_papers.items():
        papers[paper_id] = record

    for row in rows:
        paper_id = canonical_id(row)
        record = build_record(row, paper_id, now)
        record["content_hash"] = stable_payload_hash(record)
        existing = papers.get(paper_id)
        if existing is None:
            papers[paper_id] = record
            continue

        record["first_seen_at"] = existing.get("first_seen_at", record["first_seen_at"])
        record["times_seen"] = int(existing.get("times_seen", 1)) + 1
        record["notes"] = existing.get("notes", [])
        record["status"] = existing.get("status", "active")

        if len(record["abstract"]) >= len(existing.get("abstract", "")):
            papers[paper_id] = {**existing, **record, "last_seen_at": now}
        else:
            existing["last_seen_at"] = now
            existing["times_seen"] = record["times_seen"]
            existing["content_hash"] = existing.get("content_hash", stable_payload_hash(existing))
            papers[paper_id] = existing

    records = sort_records(list(papers.values()))
    summary = summarize_records(records, last_run_count)
    indexes = build_indexes(records)
    payload = {
        "meta": {
            "schema_version": SCHEMA_VERSION,
            "updated_at": now,
            "generated_by": "scripts/build_knowledge_base.py",
        },
        "summary": summary,
        "indexes": indexes,
        "papers": {record["paper_id"]: record for record in records},
    }

    kb_path.parent.mkdir(parents=True, exist_ok=True)
    kb_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(render_markdown(records, summary), encoding="utf-8")

    stats_path.parent.mkdir(parents=True, exist_ok=True)
    stats_path.write_text(render_stats_markdown(summary, indexes), encoding="utf-8")

    print(f"Built knowledge base with {summary['total_papers']} papers")
    print(f"JSON: {kb_path}")
    print(f"Markdown: {md_path}")
    print(f"Stats: {stats_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
