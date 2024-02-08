# implementation based on https://en.wikipedia.org/wiki/Heap%27s_algorithm
# Copyright Darío Clavijo 2024

from sympy import factorial
from sympy.combinatorics import Permutation

def heaps(k, A):
  if k == 1:
    yield A
  else:
    for i  in range(0,  k):
      yield from heap(k-1, A)
      if k & 1 == 0:
        A[i],A[k-1] = A[k-1],A[i]
      else:
        A[0],A[k-1] = A[k-1],A[0]


def heaps_count_swaps(k, A):
  c = 0
  if k == 1:
    return 0
  else:
    for i  in range(0,  k):
      c += heaps_count_swaps(k-1, A)
      if k & 1 == 0:
        A[i],A[k-1] = A[k-1],A[i]
      else:
        A[0],A[k-1] = A[k-1],A[0]
      c += 1
  return c


A038156 = lambda n: heaps_count_swaps(n, list(range(0,n)))

