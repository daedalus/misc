#!/usr/bin/env python
# Shors algorithm classic version
# Author Dario Clavijo 2020
# GPLv3
# example: python3 classic_shor.py 20 10000

import gmpy2
from gmpy2 import mpz
import random

GCD = gmpy2.gcd


def factor(N, g, P):
    gtmp = 1
    sol = []
    if g < N:
        for i in range(0, P):
            gtmp = gtmp * g
            if gtmp % N == 1:
                # print(i,gtmp)
                gtmp2 = g ** (i // 2)
                x1 = GCD(N, gtmp2 + 1)
                x2 = GCD(N, gtmp2 - 1)
                if x1 > 1 and x1 < N:
                    sol.append([x1, N // x1])
                    print(("sol", [x1, N // x1]))
                    break
                if x1 > 2 and x2 < N:
                    sol.append([x2, N // x2])
                    print(("sol", [x2, N // x2]))
                    break
            print(("iter:", i))
    else:
        print("g should be < N")
    return sol


import sys

bits = int(sys.argv[1])
offset = 1000
max_p = int(sys.argv[2])
s = []
N = mpz(gmpy2.next_prime(2**bits) * gmpy2.next_prime((2**bits) + offset))
# N= 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139

while not s:
    g = random.randint(2, 2**bits)
    print(("N:", N, "g:", g))
    s = factor(N, g, P=max_p)
    print(s)
