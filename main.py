#!/usr/bin/env python3
"""Entry for make.fun bounty u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

Prints one line (under 200 characters) to stdout and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt): the most
creative excuse a hardware wallet gives for refusing to sign a
transaction at 3 AM. Pure stdlib, no network at run time.
"""

import os

# The wallet's excuse, built clause by clause so each beat earns its place:
# the hour, the strike, the dark screen, the dog-token regret, the sunrise.
_CLAUSES = (
    "It's 3 AM.",
    "My buttons are on strike,",
    "my screen is dark,",
    "and the last thing I signed at this hour",
    "bought a token named after a dog.",
    "Come back at sunrise.",
)


def get_line() -> str:
    """The wallet's excuse: one line, a personality, a reason, a joke."""
    return " ".join(_CLAUSES)


def validate(line: str) -> None:
    assert isinstance(line, str) and "\n" not in line, "line must be a single line"
    assert line.strip(), "line must not be blank"
    assert 1 <= len(line) <= 200, "line must be 1-200 chars"


def output_path() -> str:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR/entry.txt by default."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    if out_dir.endswith("entry.txt"):
        return out_dir
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    line = get_line()
    validate(line)
    print(line)
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
