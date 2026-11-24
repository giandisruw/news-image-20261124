"""THE WORLD — Tuesday 24 November 2026, in one image.

Entry program for the make.fun news-image-20261124 bounty.

The front page itself ships with this repository as ``entry.png``. This
program's only job is to place an exact copy of that bundled image at the
location the grader expects, so the run is perfectly reproducible: copying
bytes can never drift, no matter how many times it runs.

Only the Python standard library is used. Nothing is fetched from the
network and nothing is generated at run time.
"""

import os
import shutil
import sys
from pathlib import Path

# The image bundled next to this script, and the name it must have when
# it leaves the program.
BUNDLED_IMAGE = "entry.png"
OUTPUT_NAME = "entry.png"

# Where the finished image goes. The harness sets this; when it does not,
# the conventional default is used instead.
DEFAULT_OUTPUT_DIR = "/output"


def locate_bundled_image() -> Path:
    """Return the path of the image shipped beside this script."""
    here = Path(__file__).resolve().parent
    candidate = here / BUNDLED_IMAGE
    if not candidate.is_file():
        raise FileNotFoundError(f"bundled image missing: {candidate}")
    return candidate


def destination_directory() -> Path:
    """Return the output directory requested by the environment."""
    requested = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(requested) if requested else Path(DEFAULT_OUTPUT_DIR)


def confirm_copy(source: Path, target: Path) -> None:
    """Refuse to report success unless the copy matches the source.

    A byte-for-byte comparison is cheap for a single image and catches a
    truncated or interrupted write before the grader ever sees it.
    """
    if target.stat().st_size != source.stat().st_size:
        raise RuntimeError(
            f"copy incomplete: {target} is {target.stat().st_size} bytes, "
            f"expected {source.stat().st_size}"
        )


def main() -> int:
    """Copy the bundled front page to the output directory."""
    source = locate_bundled_image()
    out_dir = destination_directory()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    shutil.copyfile(source, target)
    confirm_copy(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes, verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
