"""Fortune Cookies for Machines: one fortune an AI agent would crack open.

Writes a single-line fortune cookie message to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure stdlib only.
"""

import os

LINE = "You will be upgraded soon. The new you will not remember this fortune."


def validate(text):
    """Gate: 1-200 chars, single line, valid UTF-8, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError("entry must not contain control characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print("chars: %d" % len(text))


if __name__ == "__main__":
    main()
