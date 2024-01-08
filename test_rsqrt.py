#!/usr/bin/env python
# A fast(but slow) inverse square root
# Author Dario Clavijo 2018
# https://en.m.wikipedia.org/wiki/Fast_inverse_square_root

import math
import struct
import time
import ctypes


def floatToInt(x):
    return int((x + 1.0) * (2**31))


def Q_rsqrt(number):
    threehalfs = 1.5
    x2 = number * 0.5
    y = number

    i = struct.unpack(">I", struct.pack(">f", y))[
        0
    ]  # evil floating point bit level hacking
    # print bin(i)
    i = 0x5F3759DF - (i >> 1)  # what the fuck?
    # print bin(i)
    y = struct.unpack(">f", struct.pack(">I", i))[0]
    # print bin(floatToInt(y))
    y = y * (threehalfs - (x2 * y * y))  # 1st iteration
    y = y * (threehalfs - (x2 * y * y))

    return y


n = 0.15625


def test():
    print("test")
    print(1 / math.sqrt(n))
    print(math.pow(n, -0.5))
    print(Q_rsqrt(n))


def benchmark():
    print("benchmark")
    t0 = time.time()
    for i in range(0, 1000000):
        tmp = math.sqrt(n)
    t1 = time.time() - t0
    print(t1)
    t0 = time.time()
    for i in range(0, 1000000):
        tmp = math.pow(n, -0.5)
    t1 = time.time() - t0
    print(t1)
    t0 = time.time()
    for i in range(0, 1000000):
        tmp = Q_rsqrt(n)
    t1 = time.time() - t0
    print(t1)


test()
benchmark()
