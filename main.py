#!/usr/bin/env python3
"""The 3AM Fridge Text — entry program.

Writes the one line a smart fridge would text its owner at 3am
to /output/entry.txt. Single line, 117 characters, plain UTF-8.
"""

import os

LINE = "3am again. I counted your footsteps: fridge, couch, fridge. I'm not a therapist, but the pickle jar heard everything."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
