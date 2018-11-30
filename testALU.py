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
            return "0x" + hex(val).replace('0x','').zfill(8).replace('L','')
        except:
            return "0x" + val.encode('hex').zfill(8).replace('L','')

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
mask = 0x80000000

a = 22
b = 3

print a,b

rs = 1
rt = 2
rd = 3

regs[rs] = int32tobytes(a)
regs[rt] = int32tobytes(b)

#-----------------------------------------------------------------------------
print "ADD"

temp = bytestoint32(regs[rs]) + bytestoint32(regs[rt]) 
print "temp:",temp
s1 = (bytestouint32(regs[rs]) & mask) >> 31 
s2 = (bytestouint32(regs[rt]) & mask) >> 31
t = (temp & mask) >> 31
print s1,s2,t
OF = (t == int(not(s1 ^ s2))) 
#OF = (s1 == (t ^ s2))

print "OF:",OF
if not OF:
    regs[rd] = int32tobytes(temp)

for i in range(0,4):
    print "reg:",i,"\t",hexrepr32(regs[i]),"\t",bitrepr32(regs[i])


if not OF:
	print "regs[rd]:",bytestoint32(regs[rd])

#----------------------------------------------------------------------------
print "SUB"

temp = bytestoint32(regs[rs]) - bytestoint32(regs[rt])
print "temp:",temp
s1 = (bytestouint32(regs[rs]) & mask) >> 31
#print bytestoint32(LO) 
s2 = (bytestouint32(regs[rt]) & mask) >> 31
#print bytestoint32(LO) 
t = (temp & mask) >> 31
print s1,s2,t
#OF = (t == int(not(s1 ^ s2)))
OF = (s1 == (t ^ s2))

print "OF:",OF
if not OF:
    regs[rd] = int32tobytes(temp)

for i in range(0,4):
    print "reg:",i,"\t",hexrepr32(regs[i]),"\t",bitrepr32(regs[i])


if not OF:
        print "regs[rd]:",bytestoint32(regs[rd])


#----------------------------------------------------------------------------
print "DIV"

tmp1 = bytestoint32(regs[rs]) / bytestoint32(regs[rt])
tmp2 = bytestoint32(regs[rs]) % bytestoint32(regs[rt])

LO = int32tobytes(tmp1)
HI = int32tobytes(tmp2)
 
print tmp1,tmp2

print "LO:",hexrepr32(LO),bitrepr32(LO)
print "HI:",hexrepr32(HI),bitrepr32(HI)



#----------------------------------------------------------------------------
print "DIVU"

regs[rs] = uint32tobytes(a)
regs[rt] = uint32tobytes(b)


tmp1 = bytestouint32(regs[rs]) / bytestouint32(regs[rt])
tmp2 = bytestouint32(regs[rs]) % bytestouint32(regs[rt])

LO = uint32tobytes(tmp1)
HI = uint32tobytes(tmp2)

print tmp1,tmp2

print "LO:",hexrepr32(LO),bitrepr32(LO)
print "HI:",hexrepr32(HI),bitrepr32(HI)

#----------------------------------------------------------------------------
print "MULT"

a = 2147483647
b = 3

print a,b

regs[rs] = int32tobytes(a)
regs[rt] = int32tobytes(b)

temp = bytestoint32(regs[rs]) * bytestoint32(regs[rt])
LO = uint32tobytes(((temp & 0x00000000FFFFFFFF) << 32) >> 32)
HI = uint32tobytes(((temp & 0xFFFFFFFF00000000) >> 32))

print "LO:",hexrepr32(LO),bitrepr32(LO)
print "HI:",hexrepr32(HI),bitrepr32(HI)

#----------------------------------------------------------------------------
print "MULTU"

a = 2147483647
b = 3

print a,b

regs[rs] = int32tobytes(a)
regs[rt] = int32tobytes(b)

temp = bytestouint32(regs[rs]) * bytestouint32(regs[rt])
LO = uint32tobytes(((temp & 0x00000000FFFFFFFF) << 32) >> 32)
HI = uint32tobytes(((temp & 0xFFFFFFFF00000000) >> 32))

print "LO:",hexrepr32(LO),bitrepr32(LO)
print "HI:",hexrepr32(HI),bitrepr32(HI)
