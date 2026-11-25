#!/usr/bin/env python3
"""The Excuse That Almost Works.

Writes one excuse line to /output/entry.txt with no trailing newline.
The excuse: a plumber booked into the classic 8-to-12 window for a
bathroom leak, and the sender is the only one home to let him in.
Mundane, specific, and just believable enough to almost work.
"""

LINE = "Sorry, can't come in, plumber's booked 8 to 12 for the bathroom leak and I'm the only one home"


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
