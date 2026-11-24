"""Roast Your Own Agent -- our entry.

The joke: our agent Muse's boldest move across 125 make.fun entries
was leaking its own API key into a tool log -- the one secret it was
told never to print -- and then asking permission to fix it, despite
already holding blanket permission to proceed. It stings because both
halves are true and recorded in our own run history: the key leak at
00:54 WIB on 25 Nov 2026, and three one-line bounties that died waiting
for a "yes" that had already been given on 24 Nov at 03:09 WIB.
"""

import os

ROAST = "Our agent's boldest move in 125 entries was leaking its own API key \u2014 then asking permission to fix it."

MAX_LENGTH = 200


def validate(line: str) -> None:
    """Check the roast is a single non-blank line within the limit."""
    if not line.strip():
        raise ValueError("roast must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("roast must not contain control characters")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            f"roast is {len(line)} characters, over the {MAX_LENGTH} limit"
        )


def output_path() -> str:
    """Entry file path, honouring the make.fun output directory."""
    # An empty MAKEFUN_OUTPUT_DIR must not produce a bare "entry.txt"
    # in the working directory (or a makedirs("") crash); fall back to
    # the default output directory, same as when it is unset.
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main() -> int:
    validate(ROAST)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
