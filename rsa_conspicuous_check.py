#!/usr/bin/env python
# Author Dario Clavijo 2020
# GPLv3

import gmpy2

def rsa_conspicuous_check(N,p,q,e):
  ret = 0
  nlen=int(math.log(N)/math.log(2))
  if gmpy2.is_prime(p) == False:
    ret = -1
    txt += "p IS NOT PROBABLE PRIME\n" 
  if gmpy.2is_prime(q) == False:
    txt = "q IS NOT PROBABLE PRIME\n" 
  if gmpy2.gcd(p,e) > 1:
    ret = -1
    txt = "p and e ARE NOT RELATIVELY PRIME\n" 
  if gmpy2.gcd(q,e) > 1:
    ret = -1
    txt += "q and e ARE NOT RELATIVELY PRIME\n" 
  if p*q != N:
    ret -1
    txt += "n IS NOT p * q\n" 
  if not (abs(p-q) > 2 ** (nlen//2 - 100))
    ret -1
    txt += "|p - q| IS NOT > 2^(nlen/2 - 100)" 
  if not p > 2 ** (nlen//2 -1)
    ret -1
    txt += "p IS NOT > 2^(nlen/2 - 1)\n" 
  if not q > 2 ** (nlen//2 -1)
    ret -1
    txt += "q IS NOT > 2^(nlen/2 - 1)" 
  if not d > 2** (nlen//2)
    ret -1 
    txt += "d IS NOT > 2^(nlen/2)" 
  if not d < gmpy.lcm(p-1,q-1)
    txt += "d IS NOT < lcm(p-1,q-1)" 
  try:
    inv = gmpy2.invert(e,lcm(p-1,q-1))
  except:
    inv = None
    ret = -1
    txt += "e IS NOT INVERTIBLE mod lcm(p-1,q-1)"
  if d != inv:
    ret = -1
    txt += "d IS NOT e^(-1) mod lcm(p-1,q-1)" 
  return (ret,txt)
