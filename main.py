"""Entry for make.fun's "The joke about the demo" bounty.

Writes one joke about AI coding agents to /output/entry.txt.
Local run: mkdir -p out && OUTPUT=out/entry.txt python3 main.py
"""
import os

JOKE = "During the demo, my coding agent imported a library it had invented; npm's 404 was the first reviewer to leave honest feedback."

OUTPUT = os.environ.get("OUTPUT", "/output/entry.txt")

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)
