def bitrepr32(val):
        try:
            return "0b"+ bin(val).replace('0b','').zfill(32)
        except:
            tmp = ""
            for byte in val:
                tmp += bin(ord(byte)).replace('0b','')
            return "0b" + tmp.zfill(32)
def hexrepr32(val):
        try:
            return "0x" + hex(val).replace('0x','').zfill(8)
        except:
            return "0x" + val.encode('hex').zfill(8)

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

regs = [0,0,0,0]

a = 1
b = 2

print a,b

regs[1] = int32tobytes(a)
regs[2] = int32tobytes(b)

rs = 1
rt = 2
rd = 3

mask = 0x80000000

temp = bytestoint32(regs[rs]) + bytestoint32(regs[rt]) 
s1 = (bytestouint32(regs[rs]) & mask) >> 31 
s2 = (bytestouint32(regs[rt]) & mask) >> 31
t = (temp & mask) >> 31
OF = t == int(not(s1 ^ s2)) 
print "OF:",OF
if not OF:
    regs[rd] = int32tobytes(temp)

for i in range(0,4):
    print "reg:",i,"\t",hexrepr32(regs[i]),"\t",bitrepr32(regs[i])
