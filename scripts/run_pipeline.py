#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from http_utils import proxy_status_text


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the local paper-monitor pipeline.")
    parser.add_argument(
        "--skip-fetch",
        action="store_true",
        help="Skip remote fetch steps and only run offline processing.",
    )
    parser.add_argument(
        "--strict-fetch",
        action="store_true",
        help="Exit with a non-zero status if any fetch step fails.",
    )
    return parser.parse_args()


def run_step(script_name: str, check: bool = True) -> subprocess.CompletedProcess:
    script_path = ROOT / "scripts" / script_name
    print(f"==> Running {script_name}")
    return subprocess.run([sys.executable, str(script_path)], check=check)


def main() -> int:
    args = parse_args()
    print(f"Pipeline proxy mode: {proxy_status_text()}")
    fetch_failures: list[str] = []

    if not args.skip_fetch:
        for step in ("fetch_arxiv.py", "fetch_pubmed.py"):
            result = run_step(step, check=False)
            if result.returncode != 0:
                fetch_failures.append(step)

    for step in (
        "merge_rank.py",
        "enrich_papers.py",
        "summarize_digest.py",
        "build_knowledge_base.py",
        "build_embeddings.py",
        "build_site_bundle.py",
        "build_frontend.py",
    ):
        run_step(step)

    if fetch_failures:
        print(f"Fetch failures: {', '.join(fetch_failures)}", file=sys.stderr)
        if args.strict_fetch:
            return 1

    print("Pipeline completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
