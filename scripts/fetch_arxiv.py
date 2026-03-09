#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import time
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


def build_query(keywords: list[str], limit: int = 4) -> str:
    terms = []
    for keyword in keywords[:limit]:
        tokens = significant_tokens(keyword)
        variants = [f'ti:"{keyword}"', f'abs:"{keyword}"']
        if len(tokens) >= 2:
            variants.append("(" + " AND ".join(f'all:{token}' for token in tokens[:3]) + ")")
        terms.append("(" + " OR ".join(variants) + ")")
    return " OR ".join(terms)


def chunk_keywords(keywords: list[str], size: int = 4, max_chunks: int = 6) -> list[list[str]]:
    chunks = [keywords[index:index + size] for index in range(0, len(keywords), size)]
    return chunks[:max_chunks]


def fetch_entries(session: requests.Session, api_url: str, query: str, max_results: int, retries: int = 3) -> list[dict]:
    last_error: requests.RequestException | None = None
    for attempt in range(1, retries + 1):
        try:
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
        except requests.RequestException as exc:
            last_error = exc
            status_code = getattr(getattr(exc, "response", None), "status_code", None)
            if attempt >= retries or status_code not in {500, 502, 503, 504}:
                break
            time.sleep(min(6, attempt * 2))
    if last_error is not None:
        raise last_error
    return []


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


def write_output(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def main() -> int:
    args = parse_args()
    topics = load_yaml(Path(args.topics))
    sources = load_yaml(Path(args.sources))
    config = sources["sources"]["arxiv"]
    keywords = collect_keywords(topics)
    keyword_chunks = chunk_keywords(keywords)
    window_start = datetime.now(timezone.utc) - timedelta(days=config.get("days_back", 1))
    session = create_session()
    output_path = Path(args.output)

    print(f"Fetching arXiv with proxy {proxy_status_text()}")
    try:
        queries = [build_query(chunk) for chunk in keyword_chunks]
        entries = []
        for query in queries:
            print(f"arXiv batch query: {query[:160]}{'...' if len(query) > 160 else ''}")
            entries.extend(
                fetch_entries(
                    session,
                    config["api_url"],
                    query,
                    max(20, int(config.get("max_results", 100) / max(len(queries), 1))),
                )
            )
        papers = []
        seen_ids: set[str] = set()
        for entry in entries:
            paper = normalize_entry(entry)
            published = date_parser.parse(paper["date"]).astimezone(timezone.utc)
            updated = date_parser.parse(paper["updated"]).astimezone(timezone.utc)
            if max(published, updated) >= window_start and paper["arxiv_id"] not in seen_ids:
                seen_ids.add(paper["arxiv_id"])
                papers.append(paper)

        write_output(
            output_path,
            {
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "query": " || ".join(queries),
                "count": len(papers),
                "papers": papers,
                "source_statuses": [
                    {
                        "source": "arXiv",
                        "success": True,
                        "count": len(papers),
                        "error": "",
                    }
                ],
            },
        )
        print(f"Saved {len(papers)} arXiv papers to {output_path}")
        return 0
    except requests.RequestException as exc:
        write_output(
            output_path,
            {
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "query": " || ".join(build_query(chunk) for chunk in keyword_chunks),
                "count": 0,
                "papers": [],
                "source_statuses": [
                    {
                        "source": "arXiv",
                        "success": False,
                        "count": 0,
                        "error": str(exc),
                    }
                ],
            },
        )
        print(f"arXiv fetch failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.HTTPError as exc:
        print(f"HTTP error while fetching arXiv: {exc}", file=sys.stderr)
        raise SystemExit(1)
