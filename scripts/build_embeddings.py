#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
from datetime import datetime, timezone
from pathlib import Path

import requests
 
from rag_config import DEFAULT_CONFIG, load_rag_config

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KB = ROOT / "data" / "processed" / "knowledge_base.json"
DEFAULT_OUTPUT = ROOT / "data" / "processed" / "kb_embeddings.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build vector embeddings for the local paper knowledge base.")
    parser.add_argument("--kb", default=str(DEFAULT_KB))
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    return parser.parse_args()


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z0-9_+-]{2,}", text.lower())


def normalize(vec: list[float]) -> list[float]:
    norm = math.sqrt(sum(value * value for value in vec))
    if norm == 0:
        return vec
    return [value / norm for value in vec]


def local_embed(text: str, dimensions: int) -> list[float]:
    vec = [0.0] * dimensions
    tokens = tokenize(text)
    if not tokens:
        return vec
    for token in tokens:
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        index = int.from_bytes(digest[:4], "big") % dimensions
        sign = 1.0 if digest[4] % 2 == 0 else -1.0
        weight = 1.0 + min(len(token), 12) / 12.0
        vec[index] += sign * weight
    return normalize(vec)


def openai_embed_texts(texts: list[str], config: dict) -> list[list[float]]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required for provider=openai_compatible")

    response = requests.post(
        f"{config['base_url'].rstrip('/')}/embeddings",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": config["model"],
            "input": texts,
        },
        timeout=120,
    )
    response.raise_for_status()
    payload = response.json()
    data = payload.get("data", [])
    return [item["embedding"] for item in sorted(data, key=lambda item: item["index"])]


def paper_to_text(paper: dict) -> str:
    sections = [
        f"title: {paper.get('title', '')}",
        f"source: {paper.get('source', '')}",
        f"topics: {' '.join(paper.get('matched_topics', []))}",
        f"category: {paper.get('category', '')}",
        f"why: {paper.get('why_it_matters', '')}",
        f"abstract: {paper.get('abstract', '')}",
    ]
    return "\n".join(sections)


def chunked(seq: list[str], size: int) -> list[list[str]]:
    return [seq[index:index + size] for index in range(0, len(seq), size)]


def main() -> int:
    args = parse_args()
    kb = load_json(Path(args.kb))
    config = load_rag_config(Path(args.config))
    existing_index = load_json(Path(args.output))
    embedding_cfg = config.get("embedding", {})
    provider = embedding_cfg.get("provider", "local")
    dimensions = int(embedding_cfg.get("dimensions", 256))
    batch_size = int(embedding_cfg.get("batch_size", 32))
    existing_vectors = {
        item["paper_id"]: item
        for item in existing_index.get("papers", [])
        if existing_index.get("provider") == provider and existing_index.get("model", "") == embedding_cfg.get("model", "")
    }

    papers = list(kb.get("papers", {}).values())
    records = []
    to_embed_texts: list[str] = []
    to_embed_indices: list[int] = []

    for paper in papers:
        text = paper_to_text(paper)
        content_hash = paper.get("content_hash", "")
        existing = existing_vectors.get(paper["paper_id"])
        record = {
            "paper_id": paper["paper_id"],
            "title": paper.get("title", ""),
            "source": paper.get("source", ""),
            "date": paper.get("date", ""),
            "url": paper.get("url", ""),
            "matched_topics": paper.get("matched_topics", []),
            "category": paper.get("category", ""),
            "content_hash": content_hash,
            "text": text,
            "embedding": None,
        }
        if existing and existing.get("content_hash") == content_hash and existing.get("embedding"):
            record["embedding"] = existing["embedding"]
        else:
            to_embed_indices.append(len(records))
            to_embed_texts.append(text)
        records.append(record)

    new_vectors: list[list[float]] = []
    if to_embed_texts:
        if provider == "local":
            new_vectors = [local_embed(text, dimensions) for text in to_embed_texts]
        elif provider == "openai_compatible":
            for batch in chunked(to_embed_texts, batch_size):
                new_vectors.extend(openai_embed_texts(batch, embedding_cfg))
        else:
            raise ValueError(f"Unsupported embedding provider: {provider}")

    for index, vector in zip(to_embed_indices, new_vectors):
        records[index]["embedding"] = vector

    payload = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "provider": provider,
        "model": embedding_cfg.get("model", ""),
        "dimensions": len(next((item["embedding"] for item in records if item.get("embedding")), [])) or dimensions,
        "papers": records,
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    reused = len(records) - len(to_embed_texts)
    print(f"Built embeddings for {len(papers)} papers")
    print(f"Reused existing vectors: {reused}")
    print(f"New vectors: {len(to_embed_texts)}")
    print(f"Output: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
