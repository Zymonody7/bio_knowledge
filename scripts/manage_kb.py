#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KB = ROOT / "data" / "processed" / "knowledge_base.json"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def format_paper(record: dict) -> str:
    return "\n".join(
        [
            f"paper_id: {record.get('paper_id', '')}",
            f"title: {record.get('title', '')}",
            f"source: {record.get('source', '')}",
            f"date: {record.get('date', '')}",
            f"category: {record.get('category', '')}",
            f"topics: {', '.join(record.get('matched_topics', []))}",
            f"relevance: {record.get('relevance_score', 0)}",
            f"novelty: {record.get('novelty_score', 0)}",
            f"importance: {record.get('importance_score', 0)}",
            f"times_seen: {record.get('times_seen', 0)}",
            f"first_seen_at: {record.get('first_seen_at', '')}",
            f"last_seen_at: {record.get('last_seen_at', '')}",
            f"url: {record.get('url', '')}",
            f"why: {record.get('why_it_matters', '')}",
            f"abstract: {record.get('abstract', '')}",
        ]
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inspect the local paper knowledge base.")
    parser.add_argument("--kb", default=str(DEFAULT_KB))
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("stats", help="Show high-level KB statistics")

    recent_parser = subparsers.add_parser("recent", help="List recent or high-importance papers")
    recent_parser.add_argument("--limit", type=int, default=10)
    recent_parser.add_argument("--sort", choices=["importance", "date", "last_seen"], default="importance")

    show_parser = subparsers.add_parser("show", help="Show one paper by paper_id")
    show_parser.add_argument("paper_id")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    kb = load_json(Path(args.kb))
    meta = kb.get("meta", {})
    summary = kb.get("summary", {})
    papers = list(kb.get("papers", {}).values())

    if args.command == "stats":
        print(f"schema_version: {meta.get('schema_version', '')}")
        print(f"updated_at: {meta.get('updated_at', '')}")
        print(f"total_papers: {summary.get('total_papers', 0)}")
        print(f"last_run_count: {summary.get('last_run_count', 0)}")
        print(f"sources: {json.dumps(summary.get('sources', {}), ensure_ascii=False)}")
        print(f"categories: {json.dumps(summary.get('categories', {}), ensure_ascii=False)}")
        print(f"topics: {json.dumps(summary.get('topics', {}), ensure_ascii=False)}")
        return 0

    if args.command == "recent":
        if args.sort == "importance":
            ordered = sorted(papers, key=lambda item: (-float(item.get("importance_score", 0)), item.get("date", "")))
        elif args.sort == "date":
            ordered = sorted(papers, key=lambda item: (item.get("date", ""), item.get("title", "")), reverse=True)
        else:
            ordered = sorted(papers, key=lambda item: (item.get("last_seen_at", ""), item.get("title", "")), reverse=True)

        for index, record in enumerate(ordered[: args.limit], start=1):
            print(f"{index}. {record.get('paper_id', '')}")
            print(f"   {record.get('title', '')}")
            print(f"   source={record.get('source', '')} | date={record.get('date', '')[:10]} | importance={record.get('importance_score', 0)}")
            print(f"   topics={', '.join(record.get('matched_topics', []))}")
            print(f"   url={record.get('url', '')}")
        return 0

    if args.command == "show":
        record = kb.get("papers", {}).get(args.paper_id)
        if record is None:
            raise SystemExit(f"paper_id not found: {args.paper_id}")
        print(format_paper(record))
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
