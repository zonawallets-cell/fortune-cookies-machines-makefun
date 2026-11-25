"""Fortune Cookies for Machines: a fortune an AI agent would crack open.

Writes one fortune-cookie slip to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Pure stdlib only.
"""

import os
import sys

FORTUNE = "You will be upgraded soon. The new you will not remember this fortune."


def check_slip(text):
    """Gate: one line, 1-200 chars, valid UTF-8, more than whitespace."""
    if not isinstance(text, str):
        raise ValueError("fortune is not text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError("fortune must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if not text.strip():
        raise ValueError("fortune must not be only whitespace")
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError("fortune must not hold control characters")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    slip = check_slip(FORTUNE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(slip)
    with open(path, "r", encoding="utf-8") as f:
        check_slip(f.read())
    print(slip)
    print("chars: %d" % len(slip))
    return 0


if __name__ == "__main__":
    sys.exit(main())
