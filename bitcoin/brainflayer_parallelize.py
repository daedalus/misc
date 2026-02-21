#!/bin/bash
# Author Dario Clavijo 2018
import os
from subprocess import Popen
import sys

# config
binary = "code/BTC/brainflayer/brainflayer"
bloomfile = "tmp/bloom.blf"
tabfile = "tmp/tabfile.tab"
binfile = "tmp/hash160.bin"
outputfile = sys.argv[2]
h = sys.argv[1]

cmd = f"{binary} -b {bloomfile} -m {tabfile} -f {binfile} -v -a -o {outputfile} -I %s"

n = 10
for i in range(1, n + 1):
    _cmd = (cmd % h) + (" -n %d/%d" % (i, n))
    print(_cmd)
    Popen(_cmd.split(" "))
