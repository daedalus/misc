#!/usr/bin/env python
# Author Dario Clavijo 2020
# GPLv3


def count_ones(s):
    return sum(1 for i in range(0, len(s) - 1) if s[i] == "1")


d = {}
import fileinput

for line in fileinput.input():
    line = line.rstrip()
    i = int(line)
    x = bin(i).replace("0b", "")
    c = count_ones(x)
    try:
        d[c] += [i]
    except:
        d[c] = [i]

data = []
for k in dict(sorted(d.items())[::-1]):
    data.extend(iter(d[k]))
for line in data:
    print(data)
