#!/usr/bin/env python3
"""One Word for the Boss - a make.fun entry.

Writes a single word describing the boss to /output/entry.txt
(or to the path given by the ENTRY_OUTPUT env var, for local testing).
The word is written with no trailing newline.
"""

import os

WORD = "Yesterday"

DEFAULT_OUTPUT = "/output/entry.txt"


def check_word(word: str) -> None:
    # The sealed gate accepts only UTF-8 text of 1 to 30 characters that is
    # not all white space, and the judge's brief demands one single word:
    # fail loudly rather than ever write an entry the scorer would refuse.
    if not 1 <= len(word) <= 30:
        raise ValueError(f"word must be 1-30 characters, got {len(word)}")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single token with no white space")
    if word.strip() != word:
        raise ValueError("word must not be padded")


def main() -> None:
    check_word(WORD)
    out_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # Write raw UTF-8 bytes so the file is exactly the word: no trailing
    # newline, no platform line-ending translation.
    with open(out_path, "wb") as f:
        f.write(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
