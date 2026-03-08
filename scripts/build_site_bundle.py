#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KB = ROOT / "data" / "processed" / "knowledge_base.json"
DEFAULT_EMBEDDINGS = ROOT / "data" / "processed" / "kb_embeddings.json"
DEFAULT_DIGEST = ROOT / "outputs" / "daily_digest.md"
DEFAULT_OUTPUT = ROOT / "site" / "data" / "site_bundle.json"
DOCS_OUTPUT = ROOT / "docs" / "data" / "site_bundle.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a compact bundle for the static knowledge-base frontend.")
    parser.add_argument("--kb", default=str(DEFAULT_KB))
    parser.add_argument("--embeddings", default=str(DEFAULT_EMBEDDINGS))
    parser.add_argument("--digest", default=str(DEFAULT_DIGEST))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    return parser.parse_args()


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    args = parse_args()
    kb = load_json(Path(args.kb))
    embeddings = load_json(Path(args.embeddings))
    digest = load_text(Path(args.digest))
    embedding_lookup = {item["paper_id"]: item for item in embeddings.get("papers", [])}

    papers = []
    for record in kb.get("papers", {}).values():
        embedded = embedding_lookup.get(record["paper_id"], {})
        papers.append(
            {
                "paper_id": record["paper_id"],
                "title": record.get("title", ""),
                "source": record.get("source", ""),
                "date": record.get("date", ""),
                "url": record.get("url", ""),
                "category": record.get("category", ""),
                "matched_topics": record.get("matched_topics", []),
                "relevance_score": record.get("relevance_score", 0),
                "novelty_score": record.get("novelty_score", 0),
                "importance_score": record.get("importance_score", 0),
                "why_it_matters": record.get("why_it_matters", ""),
                "abstract": record.get("abstract", ""),
                "abstract_short": record.get("abstract_short", ""),
                "first_seen_at": record.get("first_seen_at", ""),
                "last_seen_at": record.get("last_seen_at", ""),
                "times_seen": record.get("times_seen", 1),
                "content_hash": record.get("content_hash", ""),
                "embedding": embedded.get("embedding", []),
                "search_text": embedded.get("text", ""),
            }
        )

    payload = {
        "meta": kb.get("meta", {}),
        "summary": kb.get("summary", {}),
        "digest_markdown": digest,
        "embedding": {
            "provider": embeddings.get("provider", ""),
            "model": embeddings.get("model", ""),
            "dimensions": embeddings.get("dimensions", 0),
            "updated_at": embeddings.get("updated_at", ""),
        },
        "papers": sorted(papers, key=lambda item: (-float(item.get("importance_score", 0)), item.get("date", ""), item.get("title", ""))),
    }

    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")

    docs_output = DOCS_OUTPUT
    docs_output.parent.mkdir(parents=True, exist_ok=True)
    docs_output.write_text(rendered, encoding="utf-8")
    print(f"Built site bundle with {len(papers)} papers")
    print(f"Output: {output_path}")
    print(f"Docs output: {docs_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
