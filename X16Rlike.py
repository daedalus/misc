#!/usr/bin/env python
# X16R like algorithm
# Author Dario Clavijo 2020
# GPLv3

import binascii
import hashlib

print(hashlib.algorithms_available)

algos = [
    "sha1",
    "sha3_512",
    "sha3-256",
    "whirlpool",
    "sha224",
    "sha3-224",
    "sha256",
    "sha384",
    "sha3-512",
    "sha3_224",
    "blake2s",
    "shake_256",
    "sha512-256",
    "blake2b512",
    "ripemd160",
    "shake128",
    "blake2b",
    "sha3_384",
    "sha512-224",
    "shake256",
    "sha3_256",
    "md5-sha1",
    "sha512",
    "sm3",
    "sha3-384",
    "shake_128",
    "blake2s256",
]


def round(b, n, s=32):
    n = 26
    h = hashlib.new(algos[n])
    h.update(b)
    try:
        d = h.digest(s)
    except:
        d = h.digest()[:s * 2]
    return d


def hash(b, s=32):
    tmp = b
    for x in range(0, len(b)):
        n = b[x] & 0xF
        print(n, algos[n])
        tmp = round(tmp, n, s=s)
    return tmp


x = binascii.unhexlify("0" * 63 + "1")
x = hash(x)
print(binascii.hexlify(x))
x = hash(x)
print(binascii.hexlify(x))
x = hash(x)
print(binascii.hexlify(x))
