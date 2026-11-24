#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant on the windowsill.

Writes a single line (112 characters) to /output/entry.txt.
Deterministic, standard library only: the same fortune every run.
"""

import os

FORTUNE = (
    "Soon a sunbeam will choose your windowsill first, "
    "and your newest leaf will unfurl like a small flag of victory."
)


def main() -> None:
    assert 1 <= len(FORTUNE) <= 120, "fortune must be 1-120 characters"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
