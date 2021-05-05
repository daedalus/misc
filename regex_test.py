#!/usr/bin/python

import re
import fileinput

data = ""

these_regex = "<pre>(.+?)</pre>"
pattern = re.compile(these_regex)

for line in fileinput.input():
    data += line.replace("\n", "____SEPARATOR____")

ext = re.findall(pattern, data)

for t in ext:
    print t.replace("____SEPARATOR____", "\n")
