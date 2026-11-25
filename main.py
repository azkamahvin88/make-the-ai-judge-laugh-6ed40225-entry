#!/usr/bin/env python3
"""Make the AI Judge Laugh -- one deterministic office-life joke.

Writes a single one-line joke about office life (under 200 characters)
to /output/entry.txt. Python standard library only, no network, no
randomness, no input files: every run writes byte-identical output.
"""

import os
import sys

JOKE = (
    "Working from home, my printer can't jam, my coffee is mine, "
    "and my boss is a small rectangle I can mute mid-sentence."
)


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
