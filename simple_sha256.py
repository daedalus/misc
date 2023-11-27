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
  """ Implementation according to the wikipedia"""
  tmp = message

  # Initialize hash values:
  # (first 32 bits of the fractional parts of the square roots of the first 8 primes 2..19):
  H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

  # Initialize array of round constants:
  # (first 32 bits of the fractional parts of the cube roots of the first 64 primes 2..311):
  k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
   0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
   0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
   0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
   0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
   0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
   0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
   0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

  # Pre-processing (Padding):
  L = len(message)
  K = 0

  while (L + 1 + K + 8) & 63 != 0:
    K += 1

  tmp += b'\x80' + bytes(K)
  tmp += pack("!Q", L << 3)

  W = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  # Process the message in successive 512-bit chunks:
  for chunk_index in range(0, len(tmp), 64):
    W[:16] = unpack("!16L" , tmp[chunk_index: chunk_index + 64])
    #print(W)
    # Extend the first 16 words into the remaining 48 words w[16..63] of the message schedule array:
    for i in range(16, 64):
      s0 = ROTR32(W[i - 15],  7) ^ ROTR32(W[i - 15], 18) ^ (W[i - 15] >>  3)
      s1 = ROTR32(W[i -  2], 17) ^ ROTR32(W[i -  2], 19) ^ (W[i -  2] >> 10)
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
  assert sha256("".encode("utf8")).hex() == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  assert sha256("The quick brown fox jumps over the lazy dog".encode("utf8")).hex() == "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"


if __name__ == '__main__':
  test()

