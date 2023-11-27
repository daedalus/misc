# pythonic bitshuffle like but slow
# it rearanges most significant bits in a byte like 8x8 or 16x16 by transposing the matrix given.
# It speedsup compression so it can be uses as a step before compressing.
# The only dependence is numpy.
# Author Dario Clavijo 2017
# License GPLv3

import numpy


def bintobit(tmp):
    tmp = numpy.frombuffer(tmp, dtype=numpy.uint8)
    tmp = numpy.unpackbits(tmp)
    return tmp


def Transpose8X8(tmp):
    tmp = bintobit(tmp)
    tmp = numpy.reshape(tmp, (8, 8))
    tmp = numpy.reshape(tmp.T, (1, 64))
    tmp = numpy.packbits(tmp)
    return tmp.tobytes()


def Transpose16X16(tmp):
    tmp = bintobit(tmp)
    tmp = numpy.reshape(tmp, (16, 16))
    tmp = numpy.reshape(tmp.T, (1, 256))
    tmp = numpy.packbits(tmp)
    return tmp.tobytes()


def bitshuffle(buff, mode):
    if len(buff) % 8 != 0:
        raise Exception("Buffer must be a multiple of 8 bytes")
    buff2 = ""
    if mode == 8:
        for i in xrange(0, len(buff) - 1, 8):
            buff2 += Transpose8X8(buff[i : i + 8])
    elif mode == 16:
        for i in xrange(0, len(buff) - 1, 16):
            buff2 += Transpose16X16(buff[i : i + 16])
    return buff2


if __name__ == "__main__":
    a = "Dario Clavijo   "
    print a, len(a)
    print a.encode("hex")
    print bintobit(a)

    a = bitshuffle(a)
    print a.encode("hex")
    print bintobit(a)
    print bitshuffle(a)
