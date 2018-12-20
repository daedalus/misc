#!/usr/bin/env python
# IEEE-754-1985
# Dario Clavijo 2018
# GPLv2
verbose = False

def ieee_754_1985_32(i):
	# single precision floating point
	# SEEEEEEEEMMMMMMMMMMMMMMMMMMMMMMM
	S = i >> 31
	E = (i >> 23) & 0b11111111
	F = (i & 0b11111111111111111111111 )
	a = (-1**S) 
        b = (1.0 + ((1.0 * F)/(2**23))) 
	c = (2**(E-127))
	if verbose:
		print bin(s),bin(E),bin(F)
		print a,b,c
	return a*b*c

def ieee_754_1985_64(i):
	# double precision floating point
	# SEEEEEEEEEEEMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	S = i >> 63
        E = (i >> 52) & 0b11111111111
        F = (i & 0b1111111111111111111111111111111111111111111111111111)
        a = (-1**S) 
	b = (1.0 + ((1.0 * F)/(2**52))) 
	c =  (2**(E-1023))
	if verbose:
	        print bin(s),bin(E),bin(F)
		print a,b,c
	return a*b*c

def test():
	pi=3.141592653589793
	print pi
	pi32=0b01000000010010010000111111011011
	pi64=0b0100000000001001001000011111101101010100010001000010110100011000
	print pi32,hex(pi32)
	print pi64,hex(pi64)
	print ieee_754_1985_32(pi32)
	print ieee_754_1985_64(pi64)

test()
