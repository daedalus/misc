#!/usr/bin/env python
# Author Dario Clavijo 2017
# Binary copy test
# GPLv3

import sys


def test(f1, f2):
    SIZE = 1024 * 128  # 128K is the optimal value for read and write buffering

    def _load(filename):
        data = ""
        with open(filename, "rb") as fp:
            recvbuf = fp.read(1024 * 128)
            while len(recvbuf) > 0:
                data += recvbuf
                recvbuf = fp.read(SIZE)
        del recvbuf
        del fp
        return data

    def _save(data, filename):
        with open(filename, "wb") as fp:
            for i in range(0, len(data) - 1, SIZE):
                fp.write(data[i : i + SIZE])
        del fp

    _save(_load(f1), f2)
    del SIZE


test(sys.argv[1], sys.argv[2])
