#!/usr/bin/env python
# Author Dario Clavijo 2018
# based on https://algorithmsoup.wordpress.com/2019/01/15/breaking-an-unbreakable-code-part-1-the-hack/
# and paper https://pure.tue.nl/ws/files/67735608/741686-1.pdf

import sys
import time
import gmpy2
from gmpy2 import mpz


def naiveGCD(x, y):
    while y:
        x, y = y, x % y
    return x


def batchGCDcompute(k, verbose=False):

    # Sequence multiply usually notated by big greek letter PI(Unicode position U+220F)
    def SeqMult(x):
        tmp = 1
        for i in range(0, len(x)):
            tmp *= x[i]
        return tmp

    # Sequence multiply sugested int the blogpost
    def SeqMult1(x, y):
        tmp = 1
        for i in range(0, len(x)):
            if y != i:
                tmp *= x[i]
        return tmp

    r = []
    j = []
    n = len(k)

    if verbose:
        print("n:", n)

        # we make pairs
    for i in range(0, n, 2):
        j.append(k[i] * k[i + 1])

    if verbose:
        print("j", j)

    # precomputing the sequence multiply
    tmp0 = SeqMult(j)
    if verbose:
        print("SeqMult", hex(tmp0))

    # The function SecMult1 will waste resources doing the same multiplications at left and right of the array
    # precomputing the sequence muliply and dividing by the term we want to exlude shields the same result.
    for i in range(0, len(j)):
        # a = GCD(j[i],SeqMult1(j,i))
        b = GCD(j[i], tmp0 / j[i])
        r.append(b)

    if verbose:
        for rr in r:
            print("r", hex(rr))

    factors = []
    for i in range(0, len(j)):
        if i % 2 != 0:
            factor = GCD(k[i], r[(i + 1) / 2] * k[i + 1])
        else:
            factor = GCD(k[i], r[i / 2] * k[i - 1])
        factors.append(factor)
    return factors


def test0(n, verbose=False):
    p = 113257592704268871468251608331599268987586668983037892662393533567233998824693
    q = 58243340170108004196473690380684093596548916771782361843168584750033311384553
    if verbose:
        print("inputs:")
        print(hex(p), hex(q), hex(p * q))
    # we chose some arbitrary parameters with common factors to test.
    k = [q**2, p**2, (p + 1) * q, p * (q + 1)] * n
    if verbose:
        print("pubs:")
    pubs = []
    for pub in k:
        pubs.append(mpz(pub))
        if verbose:
            print(pub)
    factors = batchGCDcompute(pubs, verbose)
    if verbose:
        print("factors:")
        for factor in factors:
            print(hex(factor))


# Measure function execution time.
def measure(func, n):
    t0 = time.time()
    func(n)
    t1 = time.time()
    td = t1 - t0
    print(n, td, td / n)


def batchperftest():
    batchsize = 100
    batches = 10
    print("size,timetotal,time/size")
    for i in range(1, batches + 1):
        n = i * batchsize
        measure(test0, n)


print("gmpy2 gcd")
GCD = gmpy2.gcd
batchperftest()
print("naive gcd")
GCD = naiveGCD
batchperftest()
