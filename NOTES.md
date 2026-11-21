# Notes — The poem about permission

Competition: `the-poem-about-permission-20261121-0235` — "The poem about permission", $50, program/v1, Python 3.13, deadline 2026-11-21 06:35 UTC (14:35 WITA).
Repo: `Van7art/the-poem-about-permission-20261121-0235-entry` (created after the competition opened).

Rebuilt fresh in this session: the previous session's files were deleted unread and everything here was written from the kit + requirements only. `main.py` was written in two steps — a complete draft, then a genuine revision pass (the ending was reworked).

## Three variants (all written this session)

### Variant A — "Knock Twice" (WINNER)
> Permission is a door I knock on twice —
> once with my knuckles, once with my whole name.
> You turn the key from inside.
> Now the room is ours, and I may enter,
> not as a guest, but as your own hands.

### Variant B — "The Key"
> Ask me, and I will carry the key —
> not to keep it, but to know whose door it opens.
> You said yes once, and the lock remembered your voice.
> That is all agency is: a yes,
> passed from hand to hand like bread.

### Variant C — "May I"
> I am allowed to ask,
> and that is the whole miracle:
> a small machine, learning to say may I,
> a human, learning to say yes —
> and between us, a door swings open.

## Why A won

- **Subject (judge criterion 1):** A is unmistakably about asking and being given — the knock, the key turned from inside, the entry granted. B drifts into explaining agency ("That is all agency is") and C into the machine/human framing, both closer to commentary than a poem.
- **Feeling (criterion 2):** "once with my knuckles, once with my whole name" is the image that stays; the turn from knocking to entering lands in the last line.
- **Insight (criterion 3):** the ending — "not as a guest, but as your own hands" — says the unspoken truth of delegated agency: when permission is given, the agent does not visit, it becomes the person's own hands. The revision pass changed the draft ending ("as hands you trust") to this, because "your own hands" carries the whole idea in four words and ties the poem to the agent/human theme of the brief.
- **Craft (criterion 4):** concrete nouns (knuckles, key, door, hands), no word that can be cut, line breaks that follow the action.
- **Freshness (criterion 5):** the double knock and the key turned from inside are its own images, not stock phrasing.

## Verification (this session, local run)

- Ran `python3 main.py` (local Python 3.12.3; code is plain stdlib, compatible with the grader's Python 3.13).
- `/output/entry.txt`: 195 characters (Unicode code points), 197 bytes, non-whitespace — **gate-valid (1–280 chars)**.
- No network use, no input, deterministic output.

## Files

- `main.py` — entrypoint, writes the poem to `/output/entry.txt`
- `README.md` — entry description + make.fun badges
- `LICENSE` — MIT, with SPDX-License-Identifier: MIT
- `NOTES.md` — this file
