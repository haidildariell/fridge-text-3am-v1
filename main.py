"""The 3AM Fridge Text.

Writes the one line a smart fridge would text its owner at 3am
to /output/entry.txt. One line, 1-140 characters, UTF-8.
"""

import os

# The line, kept in parts so the setup and the punchline stay editable.
OPENING = "3am. I watched you put the cake back, take it out, put it back."
MIDDLE = "I've seen this episode before."
CLOSER = "Just eat the cake, Dave."

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 140


def build_line():
    """Join the parts into the single lock-screen line."""
    parts = (OPENING, MIDDLE, CLOSER)
    line = " ".join(part for part in parts if part)
    assert MIN_LENGTH <= len(line) <= MAX_LENGTH, "line must be 1-140 chars"
    return line


def write_entry():
    """Write the line to the output file and return it."""
    line = build_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    return line


if __name__ == "__main__":
    write_entry()
