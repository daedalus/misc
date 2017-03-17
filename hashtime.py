#!/usr/bin/env python
# Author Dario Clavijo 2017

import timeit
import hashlib
import time

for h in hashlib.algorithms_available:
        def test(h):
                data=open('/dev/urandom','r').read(1024*1024)
                algo = hashlib.new(h);
                algo.update(data);
                algo.hexdigest()

        def measure(h):
                t1 = time.time() * 1000
                test(h)
                t2 = time.time() * 1000
                dt = t2-t1
                return dt

        print "%s\t%s" % (h,round(measure(h),8))
