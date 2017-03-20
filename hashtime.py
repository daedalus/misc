#!/usr/bin/env python
import timeit
import hashlib
import time

print "Algo\tSpeed"

for h in hashlib.algorithms_available:
        size = 100
        
        def test(h):
                data=open('/dev/urandom','r').read(1024*1024*size)
                algo = hashlib.new(h);
                algo.update(data);
                algo.hexdigest()

        def measure(h):
                t1 = time.time()
                test(h)
                t2 = time.time()
                dt = t2-t1
                return dt

        dt = measure(h)
        print "%s\t%s MB/s" % (h,round(size/dt,2))
