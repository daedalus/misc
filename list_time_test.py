#!/usr/bin/env python
# list insertion time test

import random
import time

list = []


def test(e, max_l):
    global list
    s1 = time.time()
    if e not in list:
        list.append(e)
    l = len(list)
    if l >= max_l:
        list = []

    s2 = time.time()
    return s2 - s1


max = 0
c = 0
acc = 0
avg = 0
acc_speed = 0
avg_speed = 0
max_l = 5000
while True:
    c = c + 1
    e = bytearray(random.getrandbits(8) for _ in range(20))

    d = test(e, max_l)

    acc += d
    speed = int(1 / d)
    acc_speed += speed

    if d > max:
        max = d
    if c % 10000 == 0:
        avg = acc / 10000
        avg_speed = acc_speed / 10000
        acc = 0
        acc_speed = 0

    print(
        "count %d, iter_time: %2.6f, max_time: %2.6f, speed: %d, avg_time: %2.6f, avg_speed: %d"
        % (
            c,
            d,
            max,
            speed,
            avg,
            avg_speed,
        )
    )
