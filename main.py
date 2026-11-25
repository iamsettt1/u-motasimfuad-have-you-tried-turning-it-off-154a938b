"""Entry for make.fun 'Have You Tried Turning It Off?'.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt.

Deterministic, stdlib only, no network.
"""

import os

LINE = "Good news \u2014 I turned it off and on again, and I can confirm the hold music is working perfectly."


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
