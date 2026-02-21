#!/usr/bin/env python
# The way the machine multiplies
# Author Dario Clavijo 2016
# GPLv3

bits = 9
multiplier = 256
multiplicand = 256

print(multiplicand, "*", multiplier)

product = 0
for i in range(0, bits):
    product += multiplicand * (multiplier & 1)
    multiplicand <<= 1
    multiplier >>= 1
    print(i, multiplicand, multiplier, product)

print("Result: ", product)
