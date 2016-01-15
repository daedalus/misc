#!/usr/bin/env python
# Author Dario Clavijo

import zlib
import bz2
import fileinput

def test(data):
        u = len(data)/2
        print "Uncompressed: {0:d}".format((u))

        for i in range(1,10):
                c = zlib.compress(data.decode('hex'),i)
                b = bz2.compress(data.decode('hex'),i)
                print "zlib compression level: {0:d}, bytes: {1:d}, ratio: {2:2.2f}".format(i, len(c), 100-len(c)/(float(u))*100)
                print "bz2  compression level: {0:d}, bytes: {1:d}, ratio: {2:2.2f}".format(i, len(b), 100-len(b)/(float(u))*100)
                                         

for line in fileinput.input():
	line = line.replace('\n','')
	test(line)
