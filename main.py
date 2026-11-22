"""FEEL-HELD entry runtime.

Writes one short relaxing text to /output/entry.txt.

Deterministic by construction: standard library only, no network,
no clock, no randomness, no environment-dependent branching —
the same bytes come out on every run.
"""

import os

# The entry text, kept as one literal so the output is exactly this string.
TEXT = (
    "The last question of the night is answered. "
    "The fans slow. "
    "Small green lights blink, patient as fireflies. "
    "The room is not empty, only quiet. "
    "Nothing is asked. "
    "Nothing is waiting. "
    "Warmth lingers a little longer in the metal."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
