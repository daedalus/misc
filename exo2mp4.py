#!/usr/bin/env python
# Instagram Exo to mp4 joiner
# Author Dario Clavijo 2018

from os import listdir, system
from os.path import isfile, join
import sys

_dir = sys.argv[1]
target = sys.argv[2]

files = [f for f in listdir(_dir) if isfile(join(_dir, f))]

# print files

parts = []
for filepart in files:
    if filepart.find(target) > -1:
        offset = filepart.split(".")[4]
        parts.append((int(offset), filepart))

for key, value in sorted(parts):
    print key, value
    system("cat %s >> %s" % (value, target))
