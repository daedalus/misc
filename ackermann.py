#!/bin/bash
# Author Dario Clavijo 2018
# Ackermann function

# naive implementation
def A(m, n):
    print ">", m, n
    if m == 0:
        print "<", m, n
        return n + 1
    if m > 0 and n == 0:
        print "<", m - 1, 1
        return A(m - 1, 1)
    if m > 0 and n > 0:
        print "<", m - 1, "A(", m, n - 1, ")"
        return A(m - 1, A(m, n - 1))
    # print "<", m,n


print A(1, 2)
print A(2, 1)
print A(2, 2)
