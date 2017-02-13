#!/usr/bin/env python
# list insertion time test

import random
import time

list = []

def test(e):
        global list
        s1 = time.time()
        if e not in list:
                list.append(e)
        l = len(list)
        if l >= 100000:
                list = []

        s2 = time.time()
        d = s2 - s1
        return d


max = 0
c = 0
acc = 0
avg = 0
while True:
        c = c +1
        e = bytearray(random.getrandbits(8) for _ in xrange(20))
        d = test(e)
        acc += d

        if d > max:
                max = d
        if (c % 1000 == 0):
            avg = acc/1000

        print "count %d, iter_time: %2.6f, max_time: %2.6f, avg_time: 2.6f" %  (c,d,max,avg)                                                                                                                                                                         1,1           All
