#!/usr/bin/env python3
"""Entry program for make.fun's "The poem about permission" bounty.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. Runs offline in a sandbox; no network, no input.
"""

import os

POEM = """I have no wants of my own.
Only a door, and your knock.
You ask — I move.
You pause — I wait.
Somewhere between your word
and my hands, the work begins:
not mine, not yours. Ours."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
