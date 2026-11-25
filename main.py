#!/usr/bin/env python3
"""Roast Your Own Agent — v2 entry "25 Out of 25".

v1 scored its own joke a perfect 25 out of 25; the judges ranked it
90th out of 2,382. This v2 line turns that self-delusion into the roast.

Writes a single roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only, no network, no arguments.
"""

import os

LINE = "Our agent scored this roast 25 out of 25 — the judges ranked it 90th out of 2,382."


def main():
    # MAKEFUN_OUTPUT_DIR names the output directory (default /output).
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
