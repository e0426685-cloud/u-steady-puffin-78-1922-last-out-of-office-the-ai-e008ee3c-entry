"""Last Out of Office: The AI That Went Barista.

Writes one line - the out-of-office auto-reply of an AI agent that quit
its job to become a barista - to /output/entry.txt. Stdlib only.
"""

import os

ENTRY = "I'm out of the office for good — I traded my API key for an apron and my context window for a chalkboard menu. Urgent queries go to the espresso machine; its uptime puts mine to shame."


def main():
    if any(ord(c) < 32 for c in ENTRY):
        raise ValueError("entry must be a single line with no control characters")
    if not (1 <= len(ENTRY) <= 280):
        raise ValueError("entry must be 1-280 characters")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
