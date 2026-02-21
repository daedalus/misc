#!/usr/bin/env python3
# Author Dario Clavijo 2021

import sys
import oeispy as op


def binet(a, b, n):
    return ((a**n) - (b**n)) / (a - b)


"""
a b resulting pol
0 2 2**n
1 3 3**n
3 5 A005059 a(n) = (5^n - 3^n)/2.
5 7 A081200 

"""


l = 20
for i in range(0, l):
    for j in range(i, l):
        tmp = []
        if i != j:
            for k in range(1, l):
                try:
                    tmp.append(str(round(binet(i, j, k))))
                except:
                    pass
            q = ",".join(tmp)
            try:
                res = op.resultEois(q)
                m = "a: %d, b: %d, Name: A%06d, Desc: %s\n" % (
                    i,
                    j,
                    op.getNumber(res[0]),
                    op.getName(res[0]),
                )
            except:
                m = ""
            sys.stderr.write(m)
            sys.stdout.write(m)
            sys.stdout.flush()
            sys.stderr.flush()
