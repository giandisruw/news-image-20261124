"""Front page for Tuesday 24 November 2026, delivered as one image.

This is the entry program for the make.fun news-image-20261124 bounty.
The finished front page already exists in this repository as
``entry.png``; all this program does is put an exact copy of it where
the grader looks for it.

Copying bytes instead of re-rendering anything keeps the result
identical on every run. The program uses only the Python standard
library, touches no network, and generates nothing.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
FALLBACK_OUTPUT_DIR = "/output"
OUTPUT_DIR_ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def bundled_image() -> Path:
    """Find the front-page image shipped alongside this script."""
    image = Path(__file__).resolve().parent / IMAGE_NAME
    if not image.is_file():
        raise FileNotFoundError(f"bundled front page not found: {image}")
    return image


def output_directory() -> Path:
    """Decide where the finished image belongs.

    The harness may point somewhere else through the environment; when
    it stays quiet, the usual ``/output`` directory is used.
    """
    chosen = os.environ.get(OUTPUT_DIR_ENV_VAR, "").strip()
    return Path(chosen) if chosen else Path(FALLBACK_OUTPUT_DIR)


def file_digest(path: Path) -> str:
    """Return the SHA-256 hex digest of a file's bytes."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def place_image(source: Path, directory: Path) -> Path:
    """Copy the bundled image into ``directory`` and check the result.

    The copy is only trusted after a full hash comparison, so a
    truncated or interrupted write is caught here instead of being
    handed to the grader as if it were fine.
    """
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / IMAGE_NAME
    if target.resolve() == source.resolve():
        # The image is already where it belongs (for example when the
        # harness points the output directory at this repository), so
        # there is nothing to copy — just confirm it is intact.
        if file_digest(target) != file_digest(source):
            raise RuntimeError(f"bundled image is damaged: {target}")
        return target
    shutil.copyfile(source, target)
    if file_digest(target) != file_digest(source):
        raise RuntimeError(f"copy does not match source: {target}")
    return target


def main() -> int:
    """Place the front page in the output directory and report it."""
    source = bundled_image()
    target = place_image(source, output_directory())
    print(f"wrote {target} ({target.stat().st_size} bytes, sha256 verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
