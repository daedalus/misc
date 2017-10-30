#!/usr/bin/env python
# Author Dario Clavijo 2016
# given a file and a csv list composed of offset,length
# we can copy the segments to other file
# or just print them in hex format for example
# we can take the binwalk csv output in fixed mode and
# dump all the findings to a file
import sys

def recovery(device,offset_list,mode,fp_dump=None):
	bytes = 32 # recovers sha256 constants or CRC32 tables in fixed mode
	iters = 8 # witch are 32*8 bytes

	for line in offset_list:
		line = line.replace('\n','').split(',')
		offset = int(line[0])
		length = int(line[1])

		if mode == "standar":
			device.seek(offset)
			data = device.read(length)
			if fp_dump:
				fp_dump.write(data)

		else if mode == "fixed":
			data = ""
			for i in range(0,iters):
				data += device.read(bytes)
			print data.encode('hex')
			if fp_dump:
				fp_dump.write(data)


device = open(sys.argv[1],'r')
offset_list = open(sys.argv[2],'r')

if len(sys.argv)>3:
	fp_dump = open(sys.argv[3],'w')
else:
	fp_dump = None

recovery(device,offset_list,'fixed',fp_dump)
