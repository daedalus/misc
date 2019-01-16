#!/usr/bin/env python
# Author Dario Clavijo 2018
# based on https://algorithmsoup.wordpress.com/2019/01/15/breaking-an-unbreakable-code-part-1-the-hack/ 
# and paper https://pure.tue.nl/ws/files/67735608/741686-1.pdf

import time
import gmpy2
from gmpy2 import mpz

def naiveGCD(x,y):
    while(y): 
        x, y = y, x % y                     
    return x 

#GCD = naiveGCD
GCD = gmpy2.gcd

def batchGCDcompute(k,verbose=False):
    def secmult(x,y):
        tmp = 1
        for i in xrange(0,len(x)):
            if y != i:
                tmp = tmp * j[i]
        return tmp

    r = []
    s = []
    j = []

    n = len(k)

    for i in xrange(0,n,2):
        j.append(k[i] + k[i+1])

    if verbose:
        print "j",j

    for i in xrange(0,len(j)):
        r.append(GCD(j[i],secmult(j,i)))

    if verbose:
        print "r",r

    for i in xrange(0,len(j)):
        if i % 2 != 0:
            tmp0 = GCD(k[i],r[(i+1)/2] * k[i+1])
        else:
            tmp0 = GCD(k[i],r[i/2] * k[i-1])
        s.append(tmp0)
    return s

a = 113257592704268871468251608331599268987586668983037892662393533567233998824693
b = 58243340170108004196473690380684093596548916771782361843168584750033311384553
ab = a*b
print "inputs:"
print hex(a),hex(b),hex(ab)

#k = [ab*a,ab*a*a,ab*ab,b*b]
def test(n,verbose=False):
    k = [a*a,b*b,ab*a,ab*b] * n
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

print "size,timetotal,time/size"
for i in range(1,100):
    n = i * 100
    t0 = time.time()
    test(n)
    t1 = time.time()
    td = t1-t0
    print i*100,td,td/n
