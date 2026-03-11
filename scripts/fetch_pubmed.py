#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

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


def collect_query_keywords(topics: dict) -> list[str]:
    topic_groups = {group.get("name"): group for group in topics.get("topic_groups", [])}
    selected = []
    seen = set()
    for name in topics.get("query_groups", []):
        group = topic_groups.get(name, {})
        for keyword in group.get("keywords", []):
            normalized = keyword.strip().lower()
            if normalized and normalized not in seen:
                seen.add(normalized)
                selected.append(keyword.strip())
    for keyword in topics.get("query_keywords", []):
        normalized = keyword.strip().lower()
        if normalized and normalized not in seen:
            seen.add(normalized)
            selected.append(keyword.strip())
    return selected or collect_keywords(topics)


def significant_tokens(keyword: str) -> list[str]:
    stopwords = {"for", "and", "the", "of", "in", "to", "ai"}
    tokens = []
    for raw in keyword.replace("/", " ").replace("-", " ").split():
        token = raw.strip().lower()
        if len(token) >= 4 and token not in stopwords:
            tokens.append(token)
    return tokens[:4]


def build_pubmed_term(keywords: list[str], limit: int = 18) -> str:
    clauses = []
    for keyword in keywords[:limit]:
        tokens = significant_tokens(keyword)
        variants = [f'"{keyword}"[Title/Abstract]']
        if len(tokens) >= 2:
            variants.append("(" + " AND ".join(f'{token}[Title/Abstract]' for token in tokens) + ")")
        clauses.append("(" + " OR ".join(variants) + ")")
    return " OR ".join(clauses)


def text_or_empty(element: ET.Element | None, path: str) -> str:
    if element is None:
        return ""
    target = element.find(path)
    return "" if target is None or target.text is None else target.text.strip()


def flatten_text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return " ".join(" ".join(element.itertext()).split())


def keyword_matches(text: str, keywords: list[str]) -> bool:
    haystack = text.lower()
    for keyword in keywords:
        lowered = keyword.lower()
        if lowered in haystack:
            return True
        tokens = significant_tokens(keyword)
        if len(tokens) >= 2 and all(token in haystack for token in tokens):
            return True
    return False


def filter_keywords_for_preprints(topics: dict) -> list[str]:
    return collect_query_keywords(topics)


def normalize_preprint_doi(value: str) -> str:
    doi = (value or "").strip()
    if not doi:
        return ""
    normalized = doi.lstrip("/")
    if normalized.startswith("10.1101/10."):
        return normalized.split("/", 1)[1]
    return normalized


def build_preprint_url(server: str, doi: str, version: str) -> str:
    normalized_server = (server or "").strip().lower() or "biorxiv"
    normalized_doi = normalize_preprint_doi(doi)
    if not normalized_doi:
        return ""
    normalized_version = str(version or "1").strip()
    return f"https://www.{normalized_server}.org/content/{normalized_doi}v{normalized_version}"


def parse_pub_date(article: ET.Element) -> str:
    pub_date = article.find(".//PubDate")
    year = text_or_empty(pub_date, "Year") or "1900"
    month = text_or_empty(pub_date, "Month") or "1"
    day = text_or_empty(pub_date, "Day") or "1"
    try:
        dt = date_parser.parse(f"{year}-{month}-{day}")
    except (ValueError, TypeError):
        dt = datetime(int(year), 1, 1)
    return dt.replace(tzinfo=timezone.utc).isoformat()


def fetch_pubmed(
    session: requests.Session,
    esearch_url: str,
    efetch_url: str,
    query: str,
    days_back: int,
    retmax: int,
) -> list[dict]:
    today = datetime.now(timezone.utc).date()
    start = today - timedelta(days=days_back)
    search_response = session.get(
        esearch_url,
        params={
            "db": "pubmed",
            "retmode": "json",
            "retmax": retmax,
            "sort": "pub date",
            "term": f"({query}) AND (\"{start}\"[Date - Publication] : \"{today}\"[Date - Publication])",
        },
        timeout=60,
        headers={"User-Agent": "paper-monitor/1.0"},
    )
    search_response.raise_for_status()
    id_list = search_response.json().get("esearchresult", {}).get("idlist", [])
    if not id_list:
        return []

    fetch_response = session.get(
        efetch_url,
        params={"db": "pubmed", "retmode": "xml", "id": ",".join(id_list)},
        timeout=60,
        headers={"User-Agent": "paper-monitor/1.0"},
    )
    fetch_response.raise_for_status()
    root = ET.fromstring(fetch_response.text)

    papers = []
    for article in root.findall(".//PubmedArticle"):
        citation = article.find("MedlineCitation")
        article_node = citation.find("Article") if citation is not None else None
        if citation is None or article_node is None:
            continue

        abstract_parts = [
            flatten_text(section)
            for section in article_node.findall("Abstract/AbstractText")
        ]
        pmid = text_or_empty(citation, "PMID")
        doi = ""
        for identifier in article.findall(".//ArticleId"):
            if identifier.attrib.get("IdType") == "doi" and identifier.text:
                doi = identifier.text.strip()
                break

        authors = []
        for author in article_node.findall("AuthorList/Author"):
            last = text_or_empty(author, "LastName")
            fore = text_or_empty(author, "ForeName")
            collective = text_or_empty(author, "CollectiveName")
            if collective:
                authors.append(collective)
            elif last or fore:
                authors.append(" ".join(part for part in [fore, last] if part))

        papers.append(
            {
                "title": flatten_text(article_node.find("ArticleTitle")),
                "source": "PubMed",
                "date": parse_pub_date(article),
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
                "abstract": " ".join(part for part in abstract_parts if part),
                "authors": authors,
                "doi": doi,
                "arxiv_id": "",
                "pubmed_id": pmid,
            }
        )

    return papers


def fetch_preprints(
    session: requests.Session,
    api_url: str,
    source_name: str,
    keywords: list[str],
    days_back: int,
    max_pages: int = 5,
) -> list[dict]:
    end_date = datetime.now(timezone.utc).date()
    start_date = end_date - timedelta(days=days_back)
    lowered_keywords = [keyword.lower() for keyword in keywords]
    papers = []
    cursor = 0
    total = None

    pages_fetched = 0
    while (total is None or cursor < total) and pages_fetched < max_pages:
        response = session.get(
            f"{api_url}/{start_date}/{end_date}/{cursor}",
            timeout=60,
            headers={"User-Agent": "paper-monitor/1.0"},
        )
        response.raise_for_status()
        payload = response.json()
        collection = payload.get("collection", [])
        messages = payload.get("messages", [])
        if total is None and messages:
            try:
                total = int(messages[0].get("total", len(collection)))
            except (TypeError, ValueError):
                total = len(collection)
        if not collection:
            break

        for item in collection:
            abstract = item.get("abstract", "") or ""
            title = item.get("title", "") or ""
            haystack = f"{title}\n{abstract}".lower()
            if not keyword_matches(haystack, lowered_keywords):
                continue

            doi = item.get("doi", "")
            server = item.get("server", source_name.lower())
            paper_date = item.get("date", "")
            try:
                paper_dt = date_parser.parse(paper_date).replace(tzinfo=timezone.utc)
            except (ValueError, TypeError):
                paper_dt = datetime.now(timezone.utc)
            papers.append(
                {
                    "title": " ".join(title.split()),
                    "source": source_name,
                    "date": paper_dt.isoformat(),
                    "url": build_preprint_url(server, doi, item.get("version", "1")) or item.get("jatsxml", ""),
                    "abstract": " ".join(abstract.split()),
                    "authors": [author.strip() for author in (item.get("authors", "") or "").split(";") if author.strip()],
                    "doi": normalize_preprint_doi(doi),
                    "arxiv_id": "",
                    "pubmed_id": "",
                }
            )

        cursor += len(collection)
        pages_fetched += 1

    return papers


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch recent PubMed and preprint papers for configured topics.")
    parser.add_argument("--topics", default=str(DEFAULT_TOPICS))
    parser.add_argument("--sources", default=str(DEFAULT_SOURCES))
    parser.add_argument("--output", default=str(RAW_DIR / "pubmed_preprints.json"))
    return parser.parse_args()


def write_output(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def main() -> int:
    args = parse_args()
    topics = load_yaml(Path(args.topics))
    sources = load_yaml(Path(args.sources))["sources"]
    keywords = collect_keywords(topics)
    query_keywords = collect_query_keywords(topics)
    preprint_keywords = filter_keywords_for_preprints(topics)
    session = create_session()
    output_path = Path(args.output)

    print(f"Fetching PubMed/preprints with proxy {proxy_status_text()}")

    papers: list[dict] = []
    source_statuses: list[dict] = []
    query = build_pubmed_term(keywords)

    pubmed_config = sources["pubmed"]
    try:
        pubmed_papers = fetch_pubmed(
            session,
        pubmed_config["esearch_url"],
        pubmed_config["efetch_url"],
        build_pubmed_term(query_keywords),
        pubmed_config.get("days_back", 1),
        pubmed_config.get("retmax", 100),
    )
        papers.extend(pubmed_papers)
        source_statuses.append(
            {"source": "PubMed", "success": True, "count": len(pubmed_papers), "error": ""}
        )
    except requests.RequestException as exc:
        source_statuses.append(
            {"source": "PubMed", "success": False, "count": 0, "error": str(exc)}
        )
        print(f"PubMed fetch failed: {exc}", file=sys.stderr)

    for source_name in ("biorxiv", "medrxiv"):
        config = sources[source_name]
        label = "bioRxiv" if source_name == "biorxiv" else "medRxiv"
        try:
            fetched = fetch_preprints(
                session,
                config["api_url"],
                label,
                preprint_keywords,
                config.get("days_back", 2),
                config.get("max_pages", 5),
            )
            papers.extend(fetched)
            source_statuses.append(
                {"source": label, "success": True, "count": len(fetched), "error": ""}
            )
        except requests.RequestException as exc:
            source_statuses.append(
                {"source": label, "success": False, "count": 0, "error": str(exc)}
            )
            print(f"{label} fetch failed: {exc}", file=sys.stderr)

    write_output(
        output_path,
        {
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "query": query,
            "count": len(papers),
            "papers": papers,
            "source_statuses": source_statuses,
        },
    )

    by_source: dict[str, int] = defaultdict(int)
    for paper in papers:
        by_source[paper.get("source", "unknown")] += 1
    print(f"Saved {len(papers)} PubMed/bioRxiv/medRxiv papers to {output_path}")
    print("Source summary:", json.dumps(by_source, ensure_ascii=False))
    return 0 if any(status["success"] for status in source_statuses) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.HTTPError as exc:
        print(f"HTTP error while fetching PubMed/preprints: {exc}", file=sys.stderr)
        raise SystemExit(1)
