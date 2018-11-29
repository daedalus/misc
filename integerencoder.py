#!/usr/bin/env python
# Author Dario Clavijo 2018

import struct
def uint32tobytes(value,big_endian=True):
	if big_endian:
		return struct.pack(">I", value)
	else:
		return struct.pack("<I", value)

def bytestouint32(value,big_endian=True):
	if big_endian:
                return struct.unpack(">I", value)
        else:
		return struct.unpack("<I", value)

def int32tobytes(value,big_endian=True):
	if big_endian:
		return struct.pack(">i", value)
	else:
		return struct.pack("<i", value)

def bytestoint32(value,big_endian=True):
	if big_endian:
                return struct.unpack(">i", value)
        else:
                return struct.unpack("<i", value)

def test():
	print uint32tobytes(0).encode('hex')
	print uint32tobytes(1).encode('hex')
	print uint32tobytes(0,False).encode('hex')
	print uint32tobytes(1,False).encode('hex')

	print int32tobytes(0).encode('hex')
	print int32tobytes(-1).encode('hex')
	print int32tobytes(0,False).encode('hex')
	print int32tobytes(-1,False).encode('hex')

test()

