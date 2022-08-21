import sys
import os
import glob
import traceback
import fnmatch

old_lyric = "Lyric=br"
new_lyric = "Lyric=R"

for file in glob.glob("*.ust"):
    base = os.path.splitext(file)[0]
    os.rename(file, base + ".txt")

for filepath in glob.iglob("./**/*.txt", recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace(old_lyric, new_lyric)
    with open(filepath, "w", encoding="utf-8", errors="ignore") as file:
        file.write(s)

for file in glob.glob("*.txt"):
    base = os.path.splitext(file)[0]
    os.rename(file, base + ".ust")
