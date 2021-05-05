#!/usr/bin/env python
# The way the machine multiplies
# Author Dario Clavijo 2016
# GPLv3

# euclids division by susbstraction
def MDIV(N, D):
    C = 0
    R = N
    while R >= D:
        R -= D
        C += 1
    return (C, R)


print MDIV(10000, 3)
