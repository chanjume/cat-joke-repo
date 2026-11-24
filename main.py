#!/usr/bin/env python3
"""Write one one-line cat joke to /output/entry.txt.

The joke: my cat walked across my keyboard at 3 a.m., typed 400
characters at random, and still shipped better code than my last
deploy. Specific and true-feeling -- 3 a.m., the keyboard walk, the
400 characters -- with the twist at the end: random paws beat my own
last deploy, the one I actually tested twice. 116 characters, one
line, no pun, retellable.
"""
import os

JOKE = "My cat walked across my keyboard at 3 a.m., typed 400 characters, and still shipped better code than my last deploy."


def main():
    assert 1 <= len(JOKE) <= 200, f"joke must be 1-200 characters, got {len(JOKE)}"
    assert JOKE.strip() == JOKE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
