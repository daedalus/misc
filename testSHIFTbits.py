#!/usr/bin/env python
# Author Dario Clavijo 2018

def SRA(val, n):
    s = val & 0x80000000
    for i in range(0,n):
        val >>= 1
        val |= s
    return val

def SLL(val,n):
    s = val & 0x80000000
    for i in range(0,n):
        val <<= 1
        #val |= 0
    return val & 0xFFFFFFFF

def SRL(val, n):
    s = val & 0x80000000
    for i in range(0,n):
        val >>= 1
        #val |= 0
    return val & 0xFFFFFFFF

def bitrepr32(val):
	return bin(val).replace('0b','').zfill(32)

def test(a,n):
	print "BIT:", bitrepr32(a)
	print "SRA:", bitrepr32(SRA(a,n)),n
	print "SRL:", bitrepr32(SRL(a,n)),n
	print "SLL:", bitrepr32(SLL(a,n)),n

n = 5
a = 0b11111111111111110000000000000000
test(a,5)
n = 5
a = 0b00000000000000001111111111111111
test(a,5)
a = 0b00000000111111111111111100000000
test(a,5)
