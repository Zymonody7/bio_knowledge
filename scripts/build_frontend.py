#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "frontend" / "src"
TARGETS = [ROOT / "site", ROOT / "docs"]
PRESERVE_DIRS = {"data"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the modular frontend source into static site/ and docs/ assets.")
    return parser.parse_args()


def clean_target(target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for child in target.iterdir():
        if child.name in PRESERVE_DIRS:
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def copy_source_tree(source: Path, destination: Path) -> None:
    for path in source.rglob("*"):
        relative = path.relative_to(source)
        output = destination / relative
        if path.is_dir():
            output.mkdir(parents=True, exist_ok=True)
            continue
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, output)


def main() -> int:
    parse_args()
    for target in TARGETS:
        clean_target(target)
        copy_source_tree(SOURCE_DIR, target)
        print(f"Built frontend into {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
