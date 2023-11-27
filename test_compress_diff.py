#!/usr/bin/env python
# Author Dario Clavijo
from lz4 import block, frame
import zlib
import random
import binascii

# main buffer
buff0 = bytearray(random.getrandbits(8) for _ in range(2048))

# tmp buffer
buff1 = bytearray(len(buff0))

# print(len(buff0))
# print(len(buff1))

# send the buffer diffs compressed
def sendbuffer():
    global buff0
    global buff1
    tmp = bytearray(len(buff0))
    for x in range(len(buff0)):
        tmp[x] = buff1[x] ^ buff0[x]
        buff1[x] = buff0[x]
    print("tmp", binascii.hexlify(tmp))
    return zlib.compress(tmp)


def modify(l):
    global buff0
    print("modifying %d random bytes" % l)
    for _ in range(l):
        buff0[random.randint(0, len(buff0) - 1)] = random.getrandbits(8)


# state 0 send
tmp = sendbuffer()
print("len compressed tmp:", len(tmp))
print("compressed:", binascii.hexlify(tmp))

# modify main buffer and send
for i in range(10, 0, -1):
    modify(2 ** i)
    tmp = sendbuffer()
    print("len compressed tmp:", len(tmp))
    print("compressed:", binascii.hexlify(tmp))
