import bitshuffle
import numpy
import sys
import time
import zlib
import lz4
import lzo
import bz2

def buff_shuffle(a):
	a = numpy.frombuffer(a)
	a = bitshuffle.bitshuffle(a).tostring()
	return a

########################
def test1():
	a = bytearray((1024**3) * 1)


	t0 = time.time()
	a = str(a).encode('zlib')
	t1 = time.time()
	print t1-t0, (len(a)//1024)

##########################
def test2():
	a = bytearray((1024**3)*1)


	t0 = time.time()
	a = buff_shuffle(a).encode('zlib')
	t1 = time.time()
	print t1-t0, (len(a) // 1024)


test1()
test2()
