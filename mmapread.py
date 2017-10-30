#!/usr/bin/env python
# Autor Dario Clavijo 2017

import re
import sys
import hexdump

pid = int(sys.argv[1])
with open("/proc/%d/maps" % pid, 'r') as maps_file:
	with open("/proc/%d/mem" % pid, 'r', 0) as mem_file:
		for line in maps_file.readlines():
			line = line.rstrip()
			cols = line.split(" ")
			print cols
			start,end = cols[0].split("-")
			start = int(start,16)
			end = int(end,16)
			mem_file.seek(start)
			chunk = mem_file.read(end - start)
			print hexdump.hexdump(chunk)

