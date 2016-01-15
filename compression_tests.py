#!/usr/bin/env python
# Author Dario Clavijo

import zlib
import bz2
import fileinput

def test(data):
	print "Uncompressed: %d" % (len(data)/2)

	for i in range(1,10):
        	c = zlib.compress(data.decode('hex'),i)
	        b = bz2.compress(data.decode('hex'),i)
        	print "zlib compression level: %d bytes: %d" % (i,len(c))
	        print "bz2  compression level: %d bytes: %d" % (i,len(b))
                                         

for line in fileinput.input():
	line = line.replace('\n','')
	test(line)
