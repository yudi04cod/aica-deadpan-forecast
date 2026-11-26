#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes a single line (at most 160 characters) to /output/entry.txt.
Deterministic: the exact same bytes on every run, no randomness,
no network, no input read from anywhere.
"""

import os

LINE = (
    "In Glintwick, a high of 41 and a 70% chance of rain falling "
    "upwards again. The mayor has asked residents to hold their "
    "umbrellas upside down."
)


def main() -> None:
    if not 1 <= len(LINE) <= 160:
        raise ValueError(f"entry line is {len(LINE)} characters, must be 1-160")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
