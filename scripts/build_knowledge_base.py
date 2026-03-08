#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PAPERS = ROOT / "outputs" / "papers.csv"
DEFAULT_KB_JSON = ROOT / "data" / "processed" / "knowledge_base.json"
DEFAULT_KB_MD = ROOT / "outputs" / "knowledge_base.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a cumulative local knowledge base from papers.csv.")
    parser.add_argument("--input", default=str(DEFAULT_PAPERS))
    parser.add_argument("--json-output", default=str(DEFAULT_KB_JSON))
    parser.add_argument("--md-output", default=str(DEFAULT_KB_MD))
    return parser.parse_args()


def load_csv_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path) -> dict:
    if not path.exists():
        return {"papers": {}}
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


def build_record(row: dict, paper_id: str) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    return {
        "paper_id": paper_id,
        "title": row.get("title", ""),
        "source": row.get("source", ""),
        "date": row.get("date", ""),
        "url": row.get("url", ""),
        "abstract": row.get("abstract", ""),
        "matched_topics": parse_topics(row.get("matched_topics", "")),
        "relevance_score": float(row.get("relevance_score") or 0),
        "novelty_score": float(row.get("novelty_score") or 0),
        "why_it_matters": row.get("why_it_matters", ""),
        "category": row.get("category", "general"),
        "doi": row.get("doi", ""),
        "arxiv_id": row.get("arxiv_id", ""),
        "pubmed_id": row.get("pubmed_id", ""),
        "updated_at": now,
        "first_seen_at": now,
    }


def render_markdown(records: list[dict]) -> str:
    category_groups: dict[str, list[dict]] = defaultdict(list)
    topic_groups: dict[str, list[dict]] = defaultdict(list)

    for record in records:
        category_groups[record["category"]].append(record)
        for topic in record["matched_topics"]:
            topic_groups[topic].append(record)

    lines = [
        "# 论文知识库",
        "",
        f"最近更新：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"累计论文数：{len(records)}",
        "",
        "## 按类别索引",
        "",
    ]

    for category in sorted(category_groups):
        rows = sorted(category_groups[category], key=lambda item: (-item["relevance_score"], item["date"], item["title"]))
        lines.append(f"### {category}")
        lines.append("")
        for row in rows:
            topics = ", ".join(row["matched_topics"]) or "未命中主题"
            lines.append(f"- [{row['title']}]({row['url']})")
            lines.append(f"  来源：{row['source']} | 日期：{row['date'][:10]} | 主题：{topics}")
            lines.append(f"  说明：{row['why_it_matters']}")
            lines.append("")

    lines.append("## 按主题索引")
    lines.append("")
    for topic in sorted(topic_groups):
        lines.append(f"### {topic}")
        lines.append("")
        for row in sorted(topic_groups[topic], key=lambda item: (-item["relevance_score"], item["date"], item["title"])):
            lines.append(f"- [{row['title']}]({row['url']}) | {row['source']} | {row['date'][:10]}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def main() -> int:
    args = parse_args()
    rows = load_csv_rows(Path(args.input))
    kb_path = Path(args.json_output)
    md_path = Path(args.md_output)
    kb = load_json(kb_path)
    papers = kb.get("papers", {})

    for row in rows:
        paper_id = canonical_id(row)
        record = build_record(row, paper_id)
        existing = papers.get(paper_id)
        if existing is None:
            papers[paper_id] = record
            continue
        record["first_seen_at"] = existing.get("first_seen_at", record["first_seen_at"])
        if len(record["abstract"]) >= len(existing.get("abstract", "")):
            papers[paper_id] = record
        else:
            existing["updated_at"] = record["updated_at"]
            papers[paper_id] = existing

    records = sorted(
        papers.values(),
        key=lambda item: (-float(item.get("relevance_score", 0)), item.get("date", ""), item.get("title", "")),
    )

    kb_path.parent.mkdir(parents=True, exist_ok=True)
    kb_path.write_text(
        json.dumps(
            {
                "updated_at": datetime.now(timezone.utc).isoformat(),
                "total_papers": len(records),
                "papers": {record["paper_id"]: record for record in records},
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(render_markdown(records), encoding="utf-8")
    print(f"Built knowledge base with {len(records)} papers")
    print(f"JSON: {kb_path}")
    print(f"Markdown: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
