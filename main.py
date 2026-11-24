#!/usr/bin/env python3
"""Write the one-line patch-note entry to the grader output directory.

The competition gate reads $MAKEFUN_OUTPUT_DIR/entry.txt and requires
UTF-8 text of 1 to 160 characters, so this script writes the entry
exactly as-is: one line, no trailing newline, no extra whitespace.
"""

import os

ENTRY = "v2.1.5: fixed a bug where a sneeze loaded to 99% then cancelled without explanation."


def main():
    if not 1 <= len(ENTRY) <= 160:
        raise ValueError("entry must be 1 to 160 characters, got %d" % len(ENTRY))
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
