#!/usr/bin/env python
# Disk IO Meter
# Dario Clavijo 2017

import os, time, zlib, binascii, random

if hasattr(os, "sync"):
    sync = os.sync
else:
    import ctypes

    libc = ctypes.CDLL("libc.so.6")

    def sync():
        libc.sync()


READSIZE = 100 * 1024 * 1024


def testread(sec_read, blocksize, filesize, fp):
    for pos in range(0, filesize, blocksize):
        sync()  # drop cache
        if sec_read:
            fp.seek(pos + blocksize)
        else:
            fp.seek(random.randint(0, READSIZE))
        fp.read(blocksize)


def measure(sec_read, blocksize, filesize, fp):
    # fp.seek(0)
    t0 = time.time()
    testread(sec_read, blocksize, filesize, fp)
    t1 = time.time()
    return t1 - t0


print "--------------------------------------------------"
fp = open("/dev/sda")
for i in range(9, 22):
    blocksize = 2 ** i
    sec_read = False
    dt = measure(sec_read, blocksize, READSIZE, fp)
    print "Bs:%d bytes\t%s MB/s\t%d IOPs sec: %s" % (
        blocksize,
        round(((READSIZE / (1024 ** 2)) / dt), 2),
        (READSIZE / blocksize) / dt,
        sec_read,
    )
