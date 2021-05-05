#!/usr/bin/env python
# Author Dario Clavijo 2020
# GPLv3
# Generate weak prime factorable with ROCA

import gmpy2


def primorial(r):
    p = 1
    tmp = 1
    for i in range(0, r):
        p = gmpy2.next_prime(p)
        tmp *= p
    return tmp


def gen_weak_prime(a, k, M):
    p = k * M + ((65537 ** a) % M)
    return p


M = primorial(47)
p = gen_weak_prime(12, 3, M)
q = gen_weak_prime(13, 4, M)

# print(p*q,p,q)
print(p * q)
