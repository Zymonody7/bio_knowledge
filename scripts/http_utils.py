#!/usr/bin/env python3
from __future__ import annotations

import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import requests


PROXY_KEYS = (
    "PROXY_URL",
    "HTTPS_PROXY",
    "HTTP_PROXY",
    "ALL_PROXY",
    "https_proxy",
    "http_proxy",
    "all_proxy",
)


def resolve_proxy_url() -> str:
    for key in PROXY_KEYS:
        value = os.environ.get(key, "").strip()
        if value:
            return value
    return ""


def create_session(user_agent: str = "paper-monitor/1.0") -> "requests.Session":
    import requests

    session = requests.Session()
    session.headers.update({"User-Agent": user_agent})

    proxy_url = os.environ.get("PROXY_URL", "").strip()
    if proxy_url:
        session.proxies.update(
            {
                "http": proxy_url,
                "https": proxy_url,
            }
        )

    return session


def proxy_status_text() -> str:
    proxy_url = resolve_proxy_url()
    if proxy_url:
        return f"enabled ({proxy_url})"
    return "disabled"
