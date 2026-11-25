"""The Battery's Last Text to Its Charger.

Writes the phone battery's final text message to the charger it waited
for all day: one line of plain text, at most 200 characters, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local tests).
"""

import os

ENTRY = (
    "hey. it's 1%. i waited all day by the outlet like a dog at the door "
    "and you went out with the OTHER phone. tell my apps i loved them. "
    "delete my search history. water my plants. goodbye."
)


def validate(text: str) -> None:
    """Enforce the competition gate: one line, 1-200 chars, not blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
