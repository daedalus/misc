#!/usr/bin/env python
# Author Dario Clavijo 2017
# GPLv3

import sys

fp = open(sys.argv[1])
fp.seek(int(sys.argv[2]))
print(fp.read(int(sys.argv[3])))
