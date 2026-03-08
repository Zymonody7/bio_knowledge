#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
DOCS_DIR = ROOT / "docs"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Mirror the static site into docs/ for branch-based GitHub Pages setups.")
    return parser.parse_args()


def copy_tree(source: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for path in source.rglob("*"):
        rel = path.relative_to(source)
        target = destination / rel
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        shutil.copy2(path, target)


def main() -> int:
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    copy_tree(SITE_DIR, DOCS_DIR)
    print(f"Synced {SITE_DIR} -> {DOCS_DIR}")
    return 0


if __name__ == "__main__":
    parse_args()
    raise SystemExit(main())
