#!/usr/bin/env python3
from __future__ import annotations

import os
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "rag.yaml"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def _apply_mapping(target: dict, mapping: dict[str, str]) -> None:
    for field, env_name in mapping.items():
        value = os.getenv(env_name, "").strip()
        if value:
            target[field] = value


def load_rag_config(path: Path | None = None) -> dict:
    config = load_yaml(path or DEFAULT_CONFIG)
    embedding = config.setdefault("embedding", {})
    chat = config.setdefault("chat", {})
    retrieval = config.setdefault("retrieval", {})

    _apply_mapping(
        embedding,
        {
            "provider": "RAG_EMBEDDING_PROVIDER",
            "model": "RAG_EMBEDDING_MODEL",
            "base_url": "RAG_EMBEDDING_BASE_URL",
            "dimensions": "RAG_EMBEDDING_DIMENSIONS",
            "batch_size": "RAG_EMBEDDING_BATCH_SIZE",
        },
    )
    _apply_mapping(
        chat,
        {
            "provider": "RAG_CHAT_PROVIDER",
            "model": "RAG_CHAT_MODEL",
            "base_url": "RAG_CHAT_BASE_URL",
            "temperature": "RAG_CHAT_TEMPERATURE",
        },
    )
    _apply_mapping(
        retrieval,
        {
            "top_k": "RAG_RETRIEVAL_TOP_K",
            "min_score": "RAG_RETRIEVAL_MIN_SCORE",
        },
    )
    return config


def resolve_site_llm_defaults(config: dict) -> dict:
    chat = config.get("chat", {})
    return {
        "base_url": os.getenv("SITE_LLM_BASE_URL", "").strip() or chat.get("base_url", ""),
        "model": os.getenv("SITE_LLM_MODEL", "").strip() or chat.get("model", ""),
    }
