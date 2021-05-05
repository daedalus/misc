#!/usr/bin/env python
# Author Dario Clavijo 2019
# function timing

import time
import operator
import random
import gmpy2
from gmpy2 import mpz


def npow(a, b):
    return a ** b


def mod(a, b):
    return a % b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mydivmod1(a, b):
    m = a / b
    r = a - (m * b)
    return m, r


def mydivmod2(a, b):
    m = operator.div(a, b)
    r = a - operator.mul(m, b)
    return m, r


def mydivmod3(a, b):
    m = gmpy2.div(a, b)
    r = a - gmpy2.mul(m, b)
    return m, r


def ndivmod(a, b):
    return divmod(a, b)


def batch(func, n):
    p = 113257592704268871468251608331599268987586668983037892662393533567233998824693
    q = 58243340170108004196473690380684093596548916771782361843168584750033311384553
    s = n * random.randint(2 ** 31, 2 ** 34)
    for i in xrange(s, n):
        func(i + 1 + p, i - 1 + q)


def measure(func_name, func, n):
    t0 = time.time()
    batch(func, n)
    t1 = time.time()
    td = t1 - t0
    print "%s: runs %d, td: %.16f, tdn: %.16f" % (func_name, n, td, td / n)


print "------------------ "
measure("native_div       ", div, 10000000)
measure("operator_div     ", operator.div, 10000000)
measure("gmpy2_div        ", gmpy2.div, 10000000)
print "------------------"
measure("native_mul       ", mul, 10000000)
measure("operator_mul     ", operator.mul, 10000000)
measure("gmpy2_mul        ", gmpy2.mul, 10000000)
print "------------------"
measure("native_divmod    ", ndivmod, 10000000)
measure("native_mydivmod  ", mydivmod1, 10000000)
measure("operator_mydivmod", mydivmod2, 10000000)
measure("gmpy2_mydivmod   ", mydivmod3, 10000000)
measure("gmpy2_t_divmod   ", gmpy2.t_divmod, 10000000)
measure("gmpy2_c_divmod   ", gmpy2.c_divmod, 10000000)
measure("gmpy2_f_divmod   ", gmpy2.f_divmod, 10000000)
print "-----------------"
measure("native_mod       ", mod, 10000000)
measure("operator_mod     ", operator.mod, 10000000)
measure("gmpy2_t_mod      ", gmpy2.t_mod, 10000000)
measure("gmpy2_f_mod      ", gmpy2.f_mod, 10000000)
measure("gmpy2_c_mod      ", gmpy2.c_mod, 10000000)
