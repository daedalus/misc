#!/bin/bash
# Author Dario Clavijo 2018
import os
from subprocess import Popen
import sys

filename = "I2"

#config
binary="code/BTC/brainflayer/brainflayer"
bloomfile="tmp/bloom.blf"
tabfile="tmp/tabfile.tab"
binfile="tmp/hash160.bin"
outputfile="tmp/brains/%s" % filename

cmd = "%s -b %s -m %s -f %s -v -a -o %s -I" % (binary,bloomfile,tabfile,binfile,outputfile) + " %s"

#print cmd
#exit(0)

mode = 2

if mode == 1:
	for i in range(0,59):
		h = "".zfill(0+i-1) + "1" + "".zfill(64-i)
		print h
		_cmd = (cmd % h)
		print _cmd
		Popen(_cmd.split(" "))
else:
	h = sys.argv[1]
	n = 10
	for i in range(1,n+1):
		_cmd = (cmd % h) + (" -n %d/%d" % (i,n))
		print _cmd
		Popen(_cmd.split(" "))
