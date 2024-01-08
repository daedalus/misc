#!/usr/bin/env python

# base point (generator)
G = (
    0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
)
# field prime
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
# order
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# I borrowed this function from from https://bitcoin.stackexchange.com/questions/25024/how-do-you-get-a-bitcoin-public-key-from-a-private-key
def sk_to_pk(sk, G, P, N):
    """
    Derive the public key of a secret key on the secp256k1 curve.
    Args:
        sk: An integer representing the secret key (also known as secret
          exponent).
    Returns:
        A coordinate (x, y) on the curve repesenting the public key
          for the given secret key.
    Raises:
        ValueError: The secret key is not in the valid range [1,N-1].
    """
    # check if the key is valid
    if not (0 < sk < N):
        msg = "{} is not a valid key (not in range [1, {}])"
        raise ValueError(msg.format(hex(sk), hex(N - 1)))

    # addition operation on the elliptic curve
    # see: https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_addition
    # note that the coordinates need to be given modulo P and that division is
    # done by computing the multiplicative inverse, which can be done with
    # x^-1 = x^(P-2) mod P using fermat's little theorem (the pow function of
    # python can do this efficiently even for very large P)
    def add(p, q):
        px, py = p
        qx, qy = q
        if p == q:
            lam = (3 * px * px) * pow(2 * py, P - 2, P)
        else:
            lam = (qy - py) * pow(qx - px, P - 2, P)
        rx = lam**2 - px - qx
        ry = lam * (px - rx) - py
        return rx % P, ry % P

    # compute G * sk with repeated addition
    # by using the binary representation of sk this can be done in 256
    # iterations (double-and-add)
    ret = None
    for i in range(256):
        if sk & (1 << i):
            ret = G if ret is None else add(ret, G)
        G = add(G, G)

    return ret


def dhtest():

    PKA = 1
    PKB = 2

    print("PKA:", hex(PKA))
    print("PKB:", hex(PKB))

    PubA = sk_to_pk(PKA, G, P, N)
    PubB = sk_to_pk(PKB, G, P, N)

    print("PubA:", hex(PubA[0]), hex(PubA[1]))
    print("PubB:", hex(PubB[0]), hex(PubB[1]))

    Q1 = sk_to_pk(PKA, PubB, P, N)
    Q2 = sk_to_pk(PKB, PubA, P, N)

    print("Shared Secret1:", hex(Q1[0]), hex(Q1[1]))
    print("Shared Secret2:", hex(Q2[0]), hex(Q2[1]))

    print(Q1 == Q2)


dhtest()
