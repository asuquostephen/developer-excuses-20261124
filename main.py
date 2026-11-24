#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks
in production (200 characters at most) to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Python 3 standard library only.
No network.
"""
import os
import sys

LINE = "It works on my machine — and since someone shipped my laptop's Docker image to production by mistake, for about three minutes it worked there too."
MAX_CHARS = 200


def check_line() -> int:
    """Return the character count of the line."""
    return len(LINE)


def main() -> int:
    if "--check" in sys.argv[1:]:
        chars = check_line()
        nbytes = len(LINE.encode("utf-8"))
        print(f"{chars} characters, {nbytes} bytes, 1 line")
        ok = 1 <= chars <= MAX_CHARS and bool(LINE.strip()) and "\n" not in LINE
        return 0 if ok else 1
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
