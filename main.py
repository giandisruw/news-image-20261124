#!/usr/bin/env python3
"""Entry program for news-image-20261124 (v2).

Copies the bundled front-page image (entry.png, in this same directory)
to the output directory as entry.png, then verifies the copy by comparing
SHA-256 hashes. The output directory comes from MAKEFUN_OUTPUT_DIR, or
defaults to /output.

Standard library only, no network. Running it twice produces
byte-identical output, because the copy is a verbatim copy of a fixed file.
"""

import hashlib
import os
import shutil
import sys

IMAGE = "entry.png"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE)
    if not os.path.isfile(src):
        print(f"error: {src} not found", file=sys.stderr)
        return 1

    out_dir = os.path.realpath(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    dst = os.path.join(out_dir, IMAGE)

    if os.path.realpath(here) == out_dir:
        print(f"already in place: {src} sha256 {sha256(src)}")
        return 0

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)

    src_hash, dst_hash = sha256(src), sha256(dst)
    print(f"source: {src} {src_hash}")
    print(f"output: {dst} {dst_hash}")
    if src_hash != dst_hash:
        print("error: output hash does not match source", file=sys.stderr)
        return 1
    print("ok: byte-identical copy")
    return 0


if __name__ == "__main__":
    sys.exit(main())
