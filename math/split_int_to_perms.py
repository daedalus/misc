"""Map a 256-bit integer onto a pair of 52-element permutations.

The 256-bit value ``n`` is split into a high part ``n1`` (``split`` bits)
and a low part ``n2`` (``256 - split`` bits). Both parts are small enough
to serve as lexicographic ranks in the symmetric group S_52 (52! ~ 2^225.7),
so each is converted into a permutation via ``Permutation.unrank_lex``.

The mapping is invertible: ranking each permutation recovers its original
bit chunk, which the assert at the bottom of ``main()`` verifies.

Usage:
    python split_int_to_perms.py

Requires: sympy

Reference: 
    https://www.johndcook.com/blog/2026/07/27/hiding-data-in-permutations/

"""

import sys
import random

from sympy.combinatorics import Permutation

# Number of elements in each permutation (S_52 ranks go up to ~2^225.7).
PERM_SIZE = 52

# Total bit-width of the input and how many of those bits go to the high half.
TOTAL_BITS = 256
SPLIT = 225  # high half: SPLIT bits; low half: TOTAL_BITS - SPLIT = 31 bits


def split_bits(n: int, split: int = SPLIT, total: int = TOTAL_BITS) -> tuple[int, int]:
    """Split integer ``n`` into a high ``split``-bit part and the remaining low part."""
    low_mask = (1 << (total - split)) - 1
    n1 = (n & ~low_mask) >> (total - split)
    n2 = n & low_mask
    return n1, n2


def rank_to_perm(rank: int) -> Permutation:
    """Convert a lexicographic rank into a permutation of ``PERM_SIZE`` elements."""
    return Permutation.unrank_lex(PERM_SIZE, rank)




def pc(p):
    for i in range(4):
        for j in range(13):
            print(chr(p[13*i + j]) + " ", end="")
        print()

def main() -> None:
    # Example value; replace with random.getrandbits(TOTAL_BITS) for random inputs.
    #n = 0xC4BBCB1FBEC99D65BF59D85C8CB62EE2DB963F0FE106F483D9AFA73BD4E39A8A
    n = int(sys.argv[1])
 
    n1, n2 = split_bits(n)
    print(n1, n2)

    a1 = rank_to_perm(n1)
    a2 = rank_to_perm(n2)
    print("a1:", a1)
    print("a2:", a2)

    s1 = Permutation.rank(a1)
    s2 = Permutation.rank(a2)

    assert s1 == n1 and s2 == n2 and n == (s1 << (TOTAL_BITS - SPLIT)) + s2
    print("round-trip verified")

    spades = list(range(0x1F0A1, 0x1F0AF))
    spades.remove(0x1F0AC) # take out the knight
    cards = [s + 16*i for s in spades for i in range(4)]

    pc(cards)
    
    p1 = a1(cards)
    p2 = a2(cards)

    pc(p1)
    pc(p2)


if __name__ == "__main__":
    main()
