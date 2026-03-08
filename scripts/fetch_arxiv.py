#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import requests
import yaml
from dateutil import parser as date_parser

from http_utils import create_session, proxy_status_text


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
DEFAULT_TOPICS = ROOT / "config" / "topics.yaml"
DEFAULT_SOURCES = ROOT / "config" / "sources.yaml"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def collect_keywords(topics: dict) -> list[str]:
    seen = set()
    keywords: list[str] = []
    for group in topics.get("topic_groups", []):
        for keyword in group.get("keywords", []):
            normalized = keyword.strip().lower()
            if normalized and normalized not in seen:
                seen.add(normalized)
                keywords.append(keyword.strip())
    return keywords


def significant_tokens(keyword: str) -> list[str]:
    stopwords = {"for", "and", "the", "of", "in", "to", "ai"}
    tokens = []
    for raw in keyword.replace("/", " ").replace("-", " ").split():
        token = raw.strip().lower()
        if len(token) >= 4 and token not in stopwords:
            tokens.append(token)
    return tokens[:4]


def build_query(keywords: list[str], limit: int = 12) -> str:
    terms = []
    for keyword in keywords[:limit]:
        tokens = significant_tokens(keyword)
        variants = [f'all:"{keyword}"']
        if len(tokens) >= 2:
            variants.append("(" + " AND ".join(f'all:"{token}"' for token in tokens) + ")")
        terms.append("(" + " OR ".join(variants) + ")")
    return " OR ".join(terms)


def fetch_entries(session: requests.Session, api_url: str, query: str, max_results: int) -> list[dict]:
    response = session.get(
        api_url,
        params={
            "search_query": query,
            "sortBy": "lastUpdatedDate",
            "sortOrder": "descending",
            "start": 0,
            "max_results": max_results,
        },
        timeout=60,
        headers={"User-Agent": "paper-monitor/1.0"},
    )
    response.raise_for_status()
    feed = feedparser.parse(response.text)
    return list(feed.entries)


def normalize_entry(entry: dict) -> dict:
    links = [link.href for link in entry.get("links", []) if getattr(link, "href", None)]
    published = date_parser.parse(entry.published).astimezone(timezone.utc)
    updated = date_parser.parse(entry.updated).astimezone(timezone.utc)
    arxiv_id = entry.id.rsplit("/", 1)[-1]
    return {
        "title": " ".join(entry.title.split()),
        "source": "arXiv",
        "date": published.isoformat(),
        "updated": updated.isoformat(),
        "url": entry.id,
        "pdf_url": next((link for link in links if "pdf" in link), ""),
        "abstract": " ".join(entry.summary.split()),
        "authors": [author.name for author in entry.get("authors", [])],
        "doi": entry.get("arxiv_doi", ""),
        "arxiv_id": arxiv_id,
        "pubmed_id": "",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch recent arXiv papers for configured topics.")
    parser.add_argument("--topics", default=str(DEFAULT_TOPICS))
    parser.add_argument("--sources", default=str(DEFAULT_SOURCES))
    parser.add_argument("--output", default=str(RAW_DIR / "arxiv.json"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    topics = load_yaml(Path(args.topics))
    sources = load_yaml(Path(args.sources))
    config = sources["sources"]["arxiv"]
    keywords = collect_keywords(topics)
    query = build_query(keywords)
    window_start = datetime.now(timezone.utc) - timedelta(days=config.get("days_back", 1))
    session = create_session()

    print(f"Fetching arXiv with proxy {proxy_status_text()}")

    entries = fetch_entries(session, config["api_url"], query, config.get("max_results", 100))
    papers = []
    for entry in entries:
        paper = normalize_entry(entry)
        published = date_parser.parse(paper["date"]).astimezone(timezone.utc)
        updated = date_parser.parse(paper["updated"]).astimezone(timezone.utc)
        if max(published, updated) >= window_start:
            papers.append(paper)

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "query": query,
                "count": len(papers),
                "papers": papers,
            },
            handle,
            ensure_ascii=False,
            indent=2,
        )

    print(f"Saved {len(papers)} arXiv papers to {output_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.HTTPError as exc:
        print(f"HTTP error while fetching arXiv: {exc}", file=sys.stderr)
        raise SystemExit(1)
