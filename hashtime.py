#!/usr/bin/env python
# Autor Dario Clavijo 2017
import sha3
import hashlib
import time

print("Algo\tSpeed")

a = list(hashlib.algorithms_available)
a.extend(("sha3_256", "sha3_512"))

for h in a:
    size = 100
    data = open("/dev/urandom", "r").read(1024 * 1024 * size)

    def test(h):
        if h == "sha3_256":
            algo = hashlib.sha3_256()
        elif h == "sha3_512":
            algo = hashlib.sha3_512()
        else:
            algo = hashlib.new(h)
        algo.update(data)
        algo.hexdigest()

    def measure(h):
        t1 = time.time()
        test(h)
        t2 = time.time()
        return t2 - t1

    dt = measure(h)
    print("%s\t%s MB/s" % (h, round(size / dt, 2)))
