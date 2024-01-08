#!/usr/bin/env python
# Author Dario Clavijo

import time

import lz4
import lzo
import lzma
import zlib
import bz2
import brotli

import fileinput


def chain_comp(data):
    return brotli.compress(
        lzma.compress(
            bz2.compress(
                zlib.compress(
                    zlib.compress(lzo.compress(lz4.compressHC(lz4.compress(data))), 1),
                    9,
                ),
                9,
            )
        )
    )


def testfunc(func, data, i=None):
    u = len(data)
    fname = str(func).split(" ")[1]
    if i:

        t0 = time.time()
        d = func.compress(data)
        t1 = time.time()
        dt = t1 - t0
        print(
            "%s compression level: %d, bytes: %d, ratio: %2.2f time: %2.8f"
            % (
                fname,
                i,
                len(d),
                100 - len(d) / (float(u)) * 100,
                dt,
            )
        )
    else:
        t0 = time.time()
        d = func.compress(data)
        t1 = time.time()
        dt = t1 - t0
        print(
            "%s compression level: 1, bytes: %d, ratio: %2.2f time: %2.8f"
            % (
                fname,
                len(d),
                100 - len(d) / (float(u)) * 100,
                dt,
            )
        )


def test(data):
    # for i in range(1,10):
    # 	testfunc(zlib,data,i)
    # 	testfunc(bz2,data,i)

    testfunc(lz4, data)
    testfunc(lzo, data)
    testfunc(lzma, data)
    testfunc(brotli, data)


def test2(data):
    u = len(data)
    t0 = time.time()
    d = chain_comp(data)
    t1 = time.time()
    dt = t1 - t0
    print(
        "chain compression level: 1, bytes: %d, ratio: %2.2f time: %2.8f"
        % (
            len(d),
            100 - len(d) / (float(u)) * 100,
            dt,
        )
    )


# test(str(bytearray((1024**2)*100)))

data = "".join(fileinput.input())
test(data)
test2(data)
