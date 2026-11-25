#!/usr/bin/env python3
"""One Line, One Laugh — u-coral-404-one-line-one-laugh-22f2c9f3.

Writes a single hilarious line to /output/entry.txt.
Gate: UTF-8 text of 1 to 200 characters, not only white space.
"""

import os

LINE = "My phone's screen time report just filed for custody of my children."


def validate(text):
    """Mirror the bounty gate: 1-200 characters, UTF-8, not only white space."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")
    return True


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
