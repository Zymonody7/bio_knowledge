#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import requests

from build_embeddings import DEFAULT_CONFIG, local_embed, tokenize
from rag_config import load_rag_config


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KB = ROOT / "data" / "processed" / "knowledge_base.json"
DEFAULT_EMBEDDINGS = ROOT / "data" / "processed" / "kb_embeddings.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search the paper knowledge base with vector retrieval and optional RAG.")
    parser.add_argument("query")
    parser.add_argument("--kb", default=str(DEFAULT_KB))
    parser.add_argument("--embeddings", default=str(DEFAULT_EMBEDDINGS))
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--top-k", type=int, default=None)
    parser.add_argument("--rag", action="store_true")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def cosine_similarity(left: list[float], right: list[float]) -> float:
    if not left or not right or len(left) != len(right):
        return 0.0
    return sum(a * b for a, b in zip(left, right))


def lexical_overlap_score(query: str, text: str) -> float:
    query_tokens = set(tokenize(query))
    text_tokens = set(tokenize(text))
    if not query_tokens or not text_tokens:
        return 0.0
    overlap = len(query_tokens & text_tokens)
    return overlap / len(query_tokens)


def embed_query(query: str, config: dict, dimensions: int) -> list[float]:
    provider = config["embedding"].get("provider", "local")
    if provider == "local":
        return local_embed(query, dimensions)

    if provider != "openai_compatible":
        raise ValueError(f"Unsupported embedding provider: {provider}")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required for provider=openai_compatible")

    response = requests.post(
        f"{config['embedding']['base_url'].rstrip('/')}/embeddings",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": config["embedding"]["model"],
            "input": query,
        },
        timeout=120,
    )
    response.raise_for_status()
    payload = response.json()
    return payload["data"][0]["embedding"]


def format_context(hit: dict, paper_lookup: dict[str, dict]) -> str:
    paper = paper_lookup.get(hit["paper_id"], {})
    topics = ", ".join(paper.get("matched_topics", [])) or "未命中主题"
    return "\n".join(
        [
            f"标题: {paper.get('title', '')}",
            f"来源: {paper.get('source', '')}",
            f"日期: {paper.get('date', '')[:10]}",
            f"主题: {topics}",
            f"分类: {paper.get('category', '')}",
            f"摘要: {paper.get('abstract', '')}",
            f"为什么重要: {paper.get('why_it_matters', '')}",
            f"链接: {paper.get('url', '')}",
        ]
    )


def rag_answer(query: str, hits: list[dict], paper_lookup: dict[str, dict], config: dict) -> str:
    chat_cfg = config.get("chat", {})
    if chat_cfg.get("provider") != "openai_compatible":
        raise ValueError("Only openai_compatible chat provider is currently supported")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required for --rag")

    contexts = []
    for index, hit in enumerate(hits, start=1):
        contexts.append(f"[文献 {index}]\n{format_context(hit, paper_lookup)}")

    system_prompt = (
        "你是一个病原生信与AI文献助手。请仅根据给定检索结果回答，"
        "优先总结与用户问题直接相关的论文，避免编造。输出中文。"
    )
    user_prompt = (
        f"用户问题：{query}\n\n"
        "下面是检索出的论文上下文：\n\n"
        + "\n\n".join(contexts)
        + "\n\n请给出：1. 简短结论 2. 最相关论文列表 3. 可继续追踪的方向。"
    )

    response = requests.post(
        f"{chat_cfg['base_url'].rstrip('/')}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": chat_cfg["model"],
            "temperature": chat_cfg.get("temperature", 0.2),
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        },
        timeout=120,
    )
    response.raise_for_status()
    payload = response.json()
    return payload["choices"][0]["message"]["content"].strip()


def main() -> int:
    args = parse_args()
    kb = load_json(Path(args.kb))
    embeddings = load_json(Path(args.embeddings))
    config = load_rag_config(Path(args.config))
    retrieval_cfg = config.get("retrieval", {})
    top_k = args.top_k or int(retrieval_cfg.get("top_k", 5))
    min_score = float(retrieval_cfg.get("min_score", 0.15))

    query_vector = embed_query(args.query, config, int(embeddings.get("dimensions", 256)))
    all_scored = []
    for item in embeddings.get("papers", []):
        semantic_score = cosine_similarity(query_vector, item.get("embedding", []))
        lexical_score = lexical_overlap_score(args.query, item.get("text", ""))
        score = semantic_score * 0.7 + lexical_score * 0.3
        all_scored.append(
            {
                **item,
                "score": score,
                "semantic_score": semantic_score,
                "lexical_score": lexical_score,
            }
        )

    all_scored.sort(key=lambda item: item["score"], reverse=True)
    hits = [item for item in all_scored if item["score"] >= min_score][:top_k]
    if not hits:
        hits = all_scored[:top_k]
    paper_lookup = kb.get("papers", {})

    print(f"Query: {args.query}")
    print(f"Hits: {len(hits)}")
    print("")
    for index, hit in enumerate(hits, start=1):
        paper = paper_lookup.get(hit["paper_id"], {})
        print(f"{index}. score={hit['score']:.3f} (semantic={hit['semantic_score']:.3f}, lexical={hit['lexical_score']:.3f}) | {paper.get('title', hit.get('title', ''))}")
        print(f"   source={paper.get('source', '')} | date={paper.get('date', '')[:10]} | category={paper.get('category', '')}")
        print(f"   url={paper.get('url', '')}")
        print(f"   why={paper.get('why_it_matters', '')}")
        print("")

    if args.rag and hits:
        print("RAG Answer")
        print("")
        print(rag_answer(args.query, hits, paper_lookup, config))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
