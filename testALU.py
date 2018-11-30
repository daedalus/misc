import sys
import struct

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


def display_regs():
	for i in range(0,len(regs)):
	    print "reg:",i,"\t",hexrepr32(regs[i]),bitrepr32(regs[i])

	print "LO:\t",hexrepr32(LO),bitrepr32(LO)
	print "HI:\t",hexrepr32(HI),bitrepr32(HI)
	print "rd:\t%d" % rd
	print "rt:\t%d" % rt
	print "rs:\t%d" % rs
	print "OF:\t%d" % OF

REGBITS = 0xFFFFFFFF #32 bit Regs
LO = 0
HI = 0
regs = [0,0,0,0,0]
mask = 0x80000000

rs = 1
rt = 2
rd = 3

#-----------------------------------------------------------------------------
# ADD
opcode = "ADD"

a = 22
b = 3

regs[rs] = int32tobytes(a)
regs[rt] = int32tobytes(b)

print opcode,a,b

temp = bytestoint32(regs[rs]) + bytestoint32(regs[rt]) 
print "temp:",temp
s1 = (bytestouint32(regs[rs]) & mask) >> 31 
s2 = (bytestouint32(regs[rt]) & mask) >> 31
t = (temp & mask) >> 31
print s1,s2,t
OF = (t == int(not(s1 ^ s2))) 

display_regs()

#-----------------------------------------------------------------------------
# ADDU
opcode = "ADDU"

a = 22
b = 3

regs[rs] = int32tobytes(a)
regs[rt] = int32tobytes(b)

print opcode,a,b

temp = bytestoint32(regs[rs]) + bytestoint32(regs[rt])% 0x7fffffff
print "temp:",temp
regs[rd] = int32tobytes(temp)

display_regs()

#----------------------------------------------------------------------------
#SUB

a = -1
b = -1

regs[rs] = int32tobytes(a)
regs[rt] = int32tobytes(b)

opcode = "SUB"
print opcode,a,b

temp = bytestoint32(regs[rs]) - bytestoint32(regs[rt])
print "temp:",temp
s1 = (bytestouint32(regs[rs]) & mask) >> 31
s2 = (bytestouint32(regs[rt]) & mask) >> 31
t = (temp & mask) >> 31
print s1,s2,t
OF = (s1 == int(not(t ^ s2)))

print "OF:",OF
if not OF:
    regs[rd] = int32tobytes(temp)

display_regs()

if not OF:
        print "regs[rd]:",bytestoint32(regs[rd])

sys.exit(0)
#----------------------------------------------------------------------------
# DIV
opcode = "DIV"
print opcode,a,b

tmp1 = bytestoint32(regs[rs]) / bytestoint32(regs[rt])
tmp2 = bytestoint32(regs[rs]) % bytestoint32(regs[rt])

LO = int32tobytes(tmp1)
HI = int32tobytes(tmp2)
 
print tmp1,tmp2

display_regs()

#----------------------------------------------------------------------------
# DIVU
opcode = "DIVU"
print opcode,a,b

regs[rs] = uint32tobytes(a)
regs[rt] = uint32tobytes(b)


tmp1 = bytestouint32(regs[rs]) / bytestouint32(regs[rt])
tmp2 = bytestouint32(regs[rs]) % bytestouint32(regs[rt])

LO = uint32tobytes(tmp1)
HI = uint32tobytes(tmp2)

print tmp1,tmp2


display_regs()

#----------------------------------------------------------------------------
# MULT
opcode = "MULT"
print opcode,a,b

a = 2147483647
b = 3

print a,b

regs[rs] = int32tobytes(a)
regs[rt] = int32tobytes(b)

temp = bytestoint32(regs[rs]) * bytestoint32(regs[rt])
LO = uint32tobytes(((temp & 0x00000000FFFFFFFF) << 32) >> 32)
HI = uint32tobytes(((temp & 0xFFFFFFFF00000000) >> 32))


display_regs()

#----------------------------------------------------------------------------
# MULTU

a = 2147483647
b = 3

opcode = "MULTU"
print opcode,a,b

regs[rs] = int32tobytes(a)
regs[rt] = int32tobytes(b)

temp = bytestouint32(regs[rs]) * bytestouint32(regs[rt])
LO = uint32tobytes(((temp & 0x00000000FFFFFFFF) << 32) >> 32)
HI = uint32tobytes(((temp & 0xFFFFFFFF00000000) >> 32))

display_regs()

#-----------------------------------------------------------------------------
# AND

opcode = "AND"
print opcode,a,b

temp = bytestouint32(regs[rs]) & bytestouint32(regs[rt])
regs[rd] = uint32tobytes(temp)

display_regs()

#-----------------------------------------------------------------------------
# OR

opcode = "OR"
print opcode,a,b

temp = bytestouint32(regs[rs]) | bytestouint32(regs[rt])
regs[rd] = uint32tobytes(temp)

display_regs()

#-----------------------------------------------------------------------------
# XOR

opcode = "XOR"
print opcode,a,b

temp = bytestouint32(regs[rs]) ^ bytestouint32(regs[rt])
regs[rd] = uint32tobytes(temp)

display_regs()

#----------------------------------------------------------------------------
# NOR

a = 2
b = 3
opcode = "NOR"
print opcode,a,b


regs[rs] = int32tobytes(a)
regs[rt] = int32tobytes(b)

temp = (bytestouint32(regs[rs]) | bytestouint32(regs[rt])) ^ REGBITS
regs[rd] = uint32tobytes(temp)

display_regs()
