import sys
import os
import glob
import traceback
import fnmatch

old_phoneme = "br"
new_phoneme = "pau"

for file in glob.glob("*.lab"):
    base = os.path.splitext(file)[0]
    os.rename(file, base + ".txt")

for filepath in glob.iglob('./**/*.txt', recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace(old_phoneme, new_phoneme)
    with open(filepath, "w") as file:
        file.write(s)

for file in glob.glob("*.txt"):
    base = os.path.splitext(file)[0]
    os.rename(file, base + ".lab")
