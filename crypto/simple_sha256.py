#!/usr/bin/env python3
# Author Dario Clavijo 2022
# GPLv3
# Based on wikipedia article https://en.wikipedia.org/wiki/SHA-2
# This implementation only uses the ALU operations: AND OR NEG SUB XOR SHIFT
# We are using the propery that op 'mod 2^n' equals to '& (n-1)'
from struct import unpack, pack


def ADD32(a, b):
    return (a + b) & 0xFFFFFFFF


def ROTR32(x, y):
    return ((x >> y) | (x << (32 - y))) & 0xFFFFFFFF


def sha256(message):
    """Implementation according to the wikipedia"""
    tmp = message

    # Initialize hash values:
    # (first 32 bits of the fractional parts of the square roots of the first 8 primes 2..19):
    H = [
        0x6A09E667,
        0xBB67AE85,
        0x3C6EF372,
        0xA54FF53A,
        0x510E527F,
        0x9B05688C,
        0x1F83D9AB,
        0x5BE0CD19,
    ]

    # Initialize array of round constants:
    # (first 32 bits of the fractional parts of the cube roots of the first 64 primes 2..311):
    k = [
        0x428A2F98,
        0x71374491,
        0xB5C0FBCF,
        0xE9B5DBA5,
        0x3956C25B,
        0x59F111F1,
        0x923F82A4,
        0xAB1C5ED5,
        0xD807AA98,
        0x12835B01,
        0x243185BE,
        0x550C7DC3,
        0x72BE5D74,
        0x80DEB1FE,
        0x9BDC06A7,
        0xC19BF174,
        0xE49B69C1,
        0xEFBE4786,
        0x0FC19DC6,
        0x240CA1CC,
        0x2DE92C6F,
        0x4A7484AA,
        0x5CB0A9DC,
        0x76F988DA,
        0x983E5152,
        0xA831C66D,
        0xB00327C8,
        0xBF597FC7,
        0xC6E00BF3,
        0xD5A79147,
        0x06CA6351,
        0x14292967,
        0x27B70A85,
        0x2E1B2138,
        0x4D2C6DFC,
        0x53380D13,
        0x650A7354,
        0x766A0ABB,
        0x81C2C92E,
        0x92722C85,
        0xA2BFE8A1,
        0xA81A664B,
        0xC24B8B70,
        0xC76C51A3,
        0xD192E819,
        0xD6990624,
        0xF40E3585,
        0x106AA070,
        0x19A4C116,
        0x1E376C08,
        0x2748774C,
        0x34B0BCB5,
        0x391C0CB3,
        0x4ED8AA4A,
        0x5B9CCA4F,
        0x682E6FF3,
        0x748F82EE,
        0x78A5636F,
        0x84C87814,
        0x8CC70208,
        0x90BEFFFA,
        0xA4506CEB,
        0xBEF9A3F7,
        0xC67178F2,
    ]

    # Pre-processing (Padding):
    L = len(message)
    K = 0

    while (L + 1 + K + 8) & 63 != 0:
        K += 1

    tmp += b"\x80" + bytes(K)
    tmp += pack("!Q", L << 3)

    W = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]

    # Process the message in successive 512-bit chunks:
    for chunk_index in range(0, len(tmp), 64):
        W[:16] = unpack("!16L", tmp[chunk_index : chunk_index + 64])
        # print(W)
        # Extend the first 16 words into the remaining 48 words w[16..63] of the message schedule array:
        for i in range(16, 64):
            s0 = ROTR32(W[i - 15], 7) ^ ROTR32(W[i - 15], 18) ^ (W[i - 15] >> 3)
            s1 = ROTR32(W[i - 2], 17) ^ ROTR32(W[i - 2], 19) ^ (W[i - 2] >> 10)
            W[i] = (W[i - 16] + s0 + W[i - 7] + s1) & 0xFFFFFFFF

        # Initialize working variables to current hash value:
        a, b, c, d, e, f, g, h = H

        # Compression function main loop:
        for i in range(64):
            S0 = ROTR32(a, 2) ^ ROTR32(a, 13) ^ ROTR32(a, 22)
            S1 = ROTR32(e, 6) ^ ROTR32(e, 11) ^ ROTR32(e, 25)
            ch = (e & f) ^ ((~e) & g)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp1 = (h + S1 + ch + k[i] + W[i]) & 0xFFFFFFFF
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        # Add the compressed chunk to the current hash value:
        H[0] = (H[0] + a) & 0xFFFFFFFF
        H[1] = (H[1] + b) & 0xFFFFFFFF
        H[2] = (H[2] + c) & 0xFFFFFFFF
        H[3] = (H[3] + d) & 0xFFFFFFFF
        H[4] = (H[4] + e) & 0xFFFFFFFF
        H[5] = (H[5] + f) & 0xFFFFFFFF
        H[6] = (H[6] + g) & 0xFFFFFFFF
        H[7] = (H[7] + h) & 0xFFFFFFFF

    # Produce the final hash value (big-endian):
    return pack("!8L", *H)


def test():
    assert (
        sha256("".encode("utf8")).hex()
        == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )
    assert (
        sha256("The quick brown fox jumps over the lazy dog".encode("utf8")).hex()
        == "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"
    )


if __name__ == "__main__":
    test()
