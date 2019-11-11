#!/usr/bin/env python
# Author Dario Clavijo 2019
# GPLv3

import binascii
import gmpy2
import sys

def inttobin(i):
    h = hex(i).replace("0x","").replace("L","")
    if (len(h) % 2 != 0):
        h = "0" + h
    return binascii.unhexlify(h)

def bintoint(i):
	return int(binascii.hexlify(i),16)

def crypt(plaintext):
	l = len(plaintext)
	n=0
	cont = True
	while cont:
		a = bintoint(plaintext + (" "*n))
		b = gmpy2.isqrt(a)
		c = b**2
		tmp = inttobin(c)
		n+=1
		cont = not (tmp[0:l] == plaintext)
	return b,n

def decrypt(cipher)
    pos = cipher.find("TRQS ")
    if pos > -1
    	pos2 = ipher.find(" ",pos)
        i = int(cipher[pos:pos2])
        s = bintoint(cipher[pos2:])
        n = s**2
        h = inttobin(h)
        return h[i:]

t = open(sys.argv[1]).read()
x,y = crypt(t)
print "TRQS",y,(inttobin(x))
