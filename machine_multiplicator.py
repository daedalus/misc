#!/usr/bin/env python
# The way the machine multiplies
# Author Dario Clavijo 2016
# GPLv3

bits = 9
multiplier = 256
multiplicand = 256

print multiplicand, "*", multiplier

product = 0
for i in range(0, bits):
    if (multiplier & 1) == 1:
        product = product + multiplicand
    multiplicand = multiplicand << 1
    multiplier = multiplier >> 1
    print i, multiplicand, multiplier, product

print "Result: ", product
