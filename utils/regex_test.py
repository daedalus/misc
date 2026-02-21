#!/usr/bin/python

import re
import fileinput

these_regex = "<pre>(.+?)</pre>"
pattern = re.compile(these_regex)

data = "".join(
    line.replace("\n", "____SEPARATOR____") for line in fileinput.input()
)
ext = re.findall(pattern, data)

for t in ext:
    print(t.replace("____SEPARATOR____", "\n"))
