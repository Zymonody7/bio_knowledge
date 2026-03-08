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
    return parser.parse_args()


def run_step(script_name: str) -> None:
    script_path = ROOT / "scripts" / script_name
    print(f"==> Running {script_name}")
    subprocess.run([sys.executable, str(script_path)], check=True)


def main() -> int:
    args = parse_args()
    print(f"Pipeline proxy mode: {proxy_status_text()}")

    steps = []
    if not args.skip_fetch:
        steps.extend(
            [
                "fetch_arxiv.py",
                "fetch_pubmed.py",
            ]
        )

    steps.extend(
        [
            "merge_rank.py",
            "summarize_digest.py",
            "build_knowledge_base.py",
            "build_embeddings.py",
            "build_site_bundle.py",
            "build_frontend.py",
        ]
    )

    for step in steps:
        run_step(step)

    print("Pipeline completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
