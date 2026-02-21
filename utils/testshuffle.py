import bitshuffle
import numpy
import sys
import time
import zlib
import lz4
import lzo
import bz2


def buff_shuffle(a):
    a = numpy.frombuffer(a)
    a = bitshuffle.bitshuffle(a).tostring()
    return a


def buff_unshuffle(buff):
    buff = numpy.frombuffer(buff)
    buff = bitshuffle.bitunshuffle(buff).tostring()
    return buff


###########################################
def test1():
    a = bytearray((1024**3) * 1)

    t0 = time.time()
    a = str(a).encode("zlib")
    t1 = time.time()
    print(t1 - t0, (len(a) // 1024))


###########################################
def test2():
    a = bytearray((1024**3) * 1)

    t0 = time.time()
    a = buff_shuffle(a).encode("zlib")
    t1 = time.time()
    print(t1 - t0, (len(a) // 1024))


###########################################
def test3():
    a = "Dario".zfill(64)
    print(a.encode("hex"))
    a = buff_shuffle(a)
    print(a.encode("hex"))
    a = buff_unshuffle(a)
    print(a.encode("hex"))


test1()
test2()
test3()
