#!/bin/bash
# Autor Dario Clavijo 2019
# simple math rsa testing
# GPLv3

import binascii
import math
import random

# ------------------------------------------------------------------------------------------

# def genprime(bits):
# 	import gmpy2
# 	p = random.randint(2**(bits-1),2**bits)
# 	while not gmpy2.is_prime(p):
# 		p = p + 2
# 	return p


def keygen():
    e = 65537
    p = 113257592704268871468251608331599268987586668983037892662393533567233998824693
    q = 58243340170108004196473690380684093596548916771782361843168584750033311384553
    # p = genprime(512)
    # q = genprime(512)
    N = p * q
    phi = (p - 1) * (q - 1)

    def inverse(x, m):
        a, b, u = 0, m, 1
        while x > 0:
            q = b // x  # integer division
            x, a, b, u = b % x, u, x, a - q * u
        if b == 1:
            return a % m

    # d = inverse_mult(1,e,phi)
    d = inverse(e, phi)
    bits = math.log(N) / math.log(2)

    return e, p, q, N, phi, d, bits


# -------------------------------------------------------------------------------------------
def keyprint(e, p, q, N, phi, d, bits):
    print "priv.p:", hex(p)
    print "priv.q:", hex(q)
    print "priv.phi:", hex(phi)
    print "priv.d:", hex(d)
    print "pub.N:", hex(N)
    print "pub.e", e
    print "pub.bits:", bits, "bytes:", int(bits / 8) + 1


# -------------------------------------------------------------------------------------------


def encrypt(text, exponent, pubkey):
    bits = math.log(pubkey) / math.log(2)
    b = int(bits / 8) + 1
    m0 = int(text.encode("hex").zfill(b), 16)
    cipher = pow(m0, exponent, pubkey)
    return cipher


def decrypt(cipher, decryptkey, pubkey):
    m1 = pow(cipher, decryptkey, pubkey)
    return m1


def test():
    plaintext = "correct horse battery staple"
    print "Plaintext input:", plaintext
    e, p, q, N, phi, d, bits = keygen()
    keyprint(e, p, q, N, phi, d, bits)
    cipher = encrypt(plaintext, e, N)
    bits = math.log(cipher) / math.log(2)
    b = int(bits / 8) + 1
    print "cipher:", hex(cipher)
    message = decrypt(cipher, d, N)
    print "message_decoded:", hex(message)
    print "Plaintext_decoded: '%s'" % binascii.unhexlify(
        hex(message).replace("0x", "").replace("L", "").zfill(b)
    )


test()
