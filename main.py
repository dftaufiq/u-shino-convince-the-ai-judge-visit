#!/usr/bin/env python3
"""Convince the AI Judge to Visit Your House: A Letter in One Image.

Writes the finished invitation to /output/entry.png. The artwork itself
lives in this repository as entry.png: a 1024 by 1024 letter drawn in code
at build time by generate_image.py (a dusk illustration of a house with a
porch chair, then a letter on cream paper inviting the AI judge to stop
judging for one evening). This entrypoint needs no network and no
third-party packages. It copies the same file on every invocation, so
repeated runs are byte-identical.

The destination is $MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

MAX_BYTES = 1024 * 1024
MAX_DIM = 1024


def source_image() -> Path:
    return Path(__file__).resolve().parent / "entry.png"


def destination_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> int:
    out = destination_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.png"
    shutil.copyfile(source_image(), target)
    size = target.stat().st_size
    print(f"copied entry.png to {target} ({size} bytes, 1024x1024)")
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB cap")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
