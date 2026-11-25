"""One Line, One Chill -- make.fun entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt. Standard library only; no network, no secrets,
no reads outside this repository.

The line: a concrete, specific image (a phone photo that should not
exist) whose dread outlasts the sentence, the smile left as the last
word so the dread lingers on it. No mirror, doll or basement cliche.
"""

from pathlib import Path

ENTRY = (
    "Every photo on my phone from last night shows me asleep in bed, "
    "except the one of me standing over my own bed, holding the camera, "
    "smiling."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.isascii(), "entry must be plain ASCII"
    assert text == text.strip() and text, "entry must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
