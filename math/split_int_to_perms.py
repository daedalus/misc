"""Map an arbitrary-size integer onto a sequence of 52-element permutations.

The integer ``n`` is extracted into limbs of ``SPLIT`` bits each (least
significant first). Since ``SPLIT = floor(log2(52!))`` = 225, every limb
is small enough to serve as a lexicographic rank in the symmetric group
S_52 (52! ~ 2^225.7), so each limb is converted into a permutation via
``Permutation.unrank_lex``. The number of limbs is derived automatically
from ``n.bit_length()``.

The mapping is invertible: ranking each permutation recovers its original
limb, and concatenating the limbs (in reverse order, ``SPLIT`` bits at a
time) recovers ``n``, which the assert at the bottom of ``main()``
verifies.

Usage:
    python split_int_to_perms.py <int>     # decimal or 0x-prefixed

Requires: sympy

Reference: 
    https://www.johndcook.com/blog/2026/07/27/hiding-data-in-permutations/

"""

import sys

from sympy.combinatorics import Permutation
from sympy import log, factorial

# Number of elements in each permutation (S_52 ranks go up to ~2^225.7).
PERM_SIZE = 52

# Bits per limb: the largest rank S_52 can represent.
SPLIT = int(log(factorial(PERM_SIZE), 2))

print(f"For {PERM_SIZE} cards we get limbs of {SPLIT} bits...")

def split_limbs(n: int, limb_bits: int = SPLIT) -> list[int]:
    """Split integer ``n`` into limbs of ``limb_bits`` bits, least significant first."""
    if n < 0:
        raise ValueError("n must be non-negative")
    mask = (1 << limb_bits) - 1
    limbs = []
    while n:
        limbs.append(n & mask)
        n >>= limb_bits
    return limbs or [0]

def join_limbs(limbs: list[int], limb_bits: int = SPLIT) -> int:
    """Reassemble limbs (least significant first) back into an integer."""
    n = 0
    for i, limb in reversed(list(enumerate(limbs))):
        assert 0 <= limb < (1 << limb_bits), f"limb {i} does not fit in {limb_bits} bits"
        n = (n << limb_bits) | limb
    return n

def rank_to_perm(rank: int) -> Permutation:
    """Convert a lexicographic rank into a permutation of ``PERM_SIZE`` elements."""
    assert 0 <= rank < factorial(PERM_SIZE), f"rank {rank} out of range for S_{PERM_SIZE}"
    return Permutation.unrank_lex(PERM_SIZE, rank)

def pc(p):
    for i in range(4):
        for j in range(13):
            print(chr(p[13*i + j]) + " ", end="")
        print()

def main() -> None:
    # Example value:
    #   0xC4BBCB1FBEC99D65BF59D85C8CB62EE2DB963F0FE106F483D9AFA73BD4E39A8A
    n = int(sys.argv[1], 0) if len(sys.argv) > 1 else 0xC4BBCB1FBEC99D65BF59D85C8CB62EE2DB963F0FE106F483D9AFA73BD4E39A8A

    limbs = split_limbs(n)
    total_bits = max(n.bit_length(), 1)
    print(f"{total_bits} bits -> {len(limbs)} limb(s) of {SPLIT} bits")
    print("limbs:", limbs)

    perms = [rank_to_perm(limb) for limb in limbs]
    for i, p in enumerate(perms):
        print(f"perm[{i}]:", p)

    ranks = [Permutation.rank(p) for p in perms]
    assert ranks == limbs and join_limbs(ranks) == n
    print("round-trip verified")

    spades = list(range(0x1F0A1, 0x1F0AF))
    spades.remove(0x1F0AC) # take out the knight
    cards = [s + 16*i for s in spades for i in range(4)]

    pc(cards)

    for i, p in enumerate(perms[:2]):
        print(f"deck permuted by perm[{i}]:")
        pc(p(cards))


if __name__ == "__main__":
    main()
