#!/usr/bin/env python3
"""Entry for make.fun bounty u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

Writes one line (under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt): the most
creative excuse a hardware wallet gives for refusing to sign a
transaction at 3 AM. Pure stdlib, no network at run time.
"""

import os

def get_line() -> str:
    """The wallet's excuse: one line, a personality, a reason, a joke."""
    return (
        "It's 3 AM. My buttons are on strike, my screen is dark, and the "
        "last thing I signed at this hour bought a token named after a dog. "
        "Come back at sunrise."
    )


def validate(line: str) -> None:
    assert isinstance(line, str) and "\n" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, "line must be 1-200 chars"


def main() -> None:
    line = get_line()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; fall back to /output/entry.txt.
    if out_dir.endswith("entry.txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
