#!/usr/bin/env python
# Author Dario Clavijo 2018
# based on https://algorithmsoup.wordpress.com/2019/01/15/breaking-an-unbreakable-code-part-1-the-hack/ 
# and paper https://pure.tue.nl/ws/files/67735608/741686-1.pdf

import sys
import time
import gmpy2
from gmpy2 import mpz

def naiveGCD(x,y):
    while(y): 
        x, y = y, x % y                     
    return x 

def batchGCDcompute(k,verbose=False):

    # Sequence multiply usually notated by big greek letter PI(Unicode position U+220F)
    def SeqMult(x):
        tmp = 1
        for i in xrange(0,len(x)):
            tmp *= x[i]
        return tmp

    # Sequence multiply sugested int the blogpost
    def SeqMult1(x,y):
        tmp = 1
        for i in xrange(0,len(x)):
            if y != i:
                tmp *= x[i]
        return tmp

    r = []
    s = []
    j = []

    n = len(k)

    # we make pairs
    for i in xrange(0,n-1,2):
        j.append(k[i] + k[i+1])

    # precomputing the sequence multiply
    tmp0 = SeqMult(j)
    if verbose:
        print tmp0

    if verbose:
        print "j",j

    # The function SecMult1 will waste resources doing the same multiplications at left and right of the array
    # precomputing the sequence muliply and dividing by the term we want to exlude shields the same result.
    for i in xrange(0,len(j)):
        #a = GCD(j[i],SeqMult1(j,i))
        b = GCD(j[i],tmp0/j[i]) 
        #if verbose:
            #print "a,b",a,b
        r.append(b)

    #sys.exit(0)

    if verbose:
        print "r",r

    for i in xrange(0,len(j)):
        if i % 2 != 0:
            tmp1 = GCD(k[i],r[(i+1)/2] * k[i+1])
        else:
            tmp1 = GCD(k[i],r[i/2] * k[i-1])
        s.append(tmp1)
    return s

def test0(n,verbose=False):
    a = 113257592704268871468251608331599268987586668983037892662393533567233998824693
    b = 58243340170108004196473690380684093596548916771782361843168584750033311384553
    if verbose:
        print "inputs:"
        print hex(a),hex(b),hex(a*b)
    # we chose some arbitrary parameters with common factors to test.
    k = [a*a,b*b,a*b*a,a*b*b] * n 
    if verbose:
        print "pubs:"
    pubs = []
    for p in k:
        pubs.append(mpz(p))
        if verbose:
            print hex(p)
    if verbose:
        print "s:"
    s = batchGCDcompute(pubs)
    if verbose:
        for p in s:
            print hex(s)

# Measure function execution time.
def measure(func,n):
    t0 = time.time()
    func(n)
    t1 = time.time()
    td = t1-t0
    print n,td,td/n

def batchperftest():
    batchsize = 100
    batches = 10
    print "size,timetotal,time/size"
    for i in range(1,batches+1):
        n = i * batchsize
        measure(test0,n)

print "gmpy2 gcd"
GCD = gmpy2.gcd
batchperftest()
print "naive gcd"
GCD = naiveGCD
batchperftest()
