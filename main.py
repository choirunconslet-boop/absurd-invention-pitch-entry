"""One-sentence absurd invention pitch for the make.fun
'One-Sentence Absurd Invention Pitch' bounty.

Writes a single sentence pitching a ridiculous invention
that fixes a tiny everyday annoyance to /output/entry.txt.
"""

import os

PITCH = (
    "A houseplant that calls in sick for you every time you "
    "forget to water it, so at least one of you finally gets a day off."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
