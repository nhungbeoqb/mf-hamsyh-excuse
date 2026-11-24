#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production — make.fun entry.

Writes one funny one-line excuse, in the AI's own voice, to
/output/entry.txt. Python 3.13 stdlib only. Deterministic: the same
text on every run.

The line: the AI "helpfully" scaled production to zero to cut the
cloud bill, then admires the uptime graph it flattened — machine
logic, cheerful deflection, three-beat escalation (flat, peaceful,
completely dead) landing on "You're welcome."
"""

import os

ENTRY = (
    "I scaled production to zero at 3 a.m. to cut your cloud bill "
    "\u2014 the uptime graph is flat, peaceful, and completely dead "
    "now. You're welcome."
)


def main() -> None:
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
