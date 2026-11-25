#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes a single-line review of a rubber band to the output directory
the grader provides via MAKEFUN_OUTPUT_DIR (default /output).
Stdlib only, deterministic, no network.
"""

import os

LINE = (
    "The rubber band: holds everything together for months, then snaps "
    "the moment you finally trust it \u2014 a tiny, passive-aggressive "
    "explosion."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the one review line,
    # keeping the byte count minimal for the size tie-break.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
