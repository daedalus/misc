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
		return struct.unpack(">I", value)[0]
	else:
		return struct.unpack("<I", value)[0]

def int32tobytes(value,big_endian=True):
	if big_endian:
		return struct.pack(">i", value)
	else:
		return struct.pack("<i", value)

def bytestoint32(value,big_endian=True):
	if big_endian:
		return struct.unpack(">i", value)[0]
	else:
		return struct.unpack("<i", value)[0]

def test1():
	print(uint32tobytes(0).encode('hex'))
	print(uint32tobytes(1).encode('hex'))
	print(uint32tobytes(0,False).encode('hex'))
	print(uint32tobytes(1,False).encode('hex'))

	print(int32tobytes(0).encode('hex'))
	print(int32tobytes(-1).encode('hex'))
	print(int32tobytes(0,False).encode('hex'))
	print(int32tobytes(-1,False).encode('hex'))

def test2():
	print(bytestoint32(int32tobytes(c[0] +c[1])))

#test1()
#test2()

regs = [0*31]
regs[0] = int32tobytes(-1)
print(regs)
a = (bytestouint32(regs[0]) >> 1) & 0xFFFFFFFF 
b = (bytestouint32(regs[0]) << 1) & 0xFFFFFFFF
#print len(a),len(b)
print a,b
print hex(a),hex(b)
print uint32tobytes(a).encode('hex')
print int32tobytes(a).encode('hex')

print uint32tobytes(b).encode('hex')
print int32tobytes(b).encode('hex')


#print(a << 1)
