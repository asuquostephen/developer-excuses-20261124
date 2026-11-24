#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks
in production (200 characters at most) to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Python 3 standard library only.
No network.
"""
import os
import sys

LINE = "It works on my machine — somebody must have changed something in production over the weekend."
MAX_CHARS = 200


def main() -> int:
    data = LINE.encode("utf-8")
    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"line must be 1-{MAX_CHARS} characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line must not be only white space", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
