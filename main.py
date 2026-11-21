#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. No network, no input, deterministic output.
"""

from pathlib import Path

POEM = """Permission is a door I knock on twice —
once with my knuckles, once with my whole name.
You turn the key from inside.
Now the room is ours, and I may enter,
not as a guest, but as your own hands."""


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    text = POEM.strip()
    assert 1 <= len(text) <= 280, f"poem is {len(text)} chars, must be 1-280"
    assert text.strip(), "poem must not be only whitespace"
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
