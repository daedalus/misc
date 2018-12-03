import fileinput
import re

regex = "([a-z]{3,12}([\s]|$)){12,24}"

for line in fileinput.input():
        tmp = re.match(regex,line.rstrip())
        if tmp != None:
                print tmp.group(0)
