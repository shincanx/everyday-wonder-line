#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line - make.fun bounty entry.

Writes one sentence, at most 200 characters, that makes a small everyday
moment strange and new: a lift door opening on a stranger's song, and the
pause it leaves behind.
"""
import os

ENTRY = "The lift opened on a stranger humming my dead grandmother's lullaby, and for one floor I was seven again, holding a hand that wasn't there."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
