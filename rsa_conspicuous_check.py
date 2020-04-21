#!/usr/bin/env python
# Author Dario Clavijo 2020
# GPLv3

import gmpy2
import math
import sys

def rsa_conspicuous_check(N,p,q,d,e):
  ret = 0
  txt = ""
  nlen=int(math.log(N)/math.log(2))
  if gmpy2.is_prime(p) == False:
    ret = -1
    txt += "p IS NOT PROBABLE PRIME\n" 
  if gmpy2.is_prime(q) == False:
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
  if not (abs(p-q) > (2 ** (nlen//2 - 100))):
    ret -1
    txt += "|p - q| IS NOT > 2^(nlen/2 - 100)\n" 
  if not (p > 2 ** (nlen//2 -1)):
    ret -1
    txt += "p IS NOT > 2^(nlen/2 - 1)\n" 
  if not (q > 2 ** (nlen//2 -1)):
    ret -1
    txt += "q IS NOT > 2^(nlen/2 - 1)\n" 
  if not (d > 2** (nlen//2)):
    ret -1 
    txt += "d IS NOT > 2^(nlen/2)\n" 
  if not (d < gmpy2.lcm(p-1,q-1)):
    txt += "d IS NOT < lcm(p-1,q-1)\n" 
  try:
    inv = gmpy2.invert(e,lcm(p-1,q-1))
  except:
    inv = None
    ret = -1
    txt += "e IS NOT INVERTIBLE mod lcm(p-1,q-1)\n"
  if d != inv:
    ret = -1
    txt += "d IS NOT e^(-1) mod lcm(p-1,q-1)" 
  return (ret,txt)

N = 316261368912034372675763445966723947266774344998810856180818351533513143408311066715404168221570429244943608807202768750419814119768169538716460558822819 
p = 58369550286914167474111748541510689816450004536626042802697414913369987394419 
q = 5418259475316478646085475045771606831413402184064804926300497557405242083601
e = 65537
phi = (p-1)*(q-1)
d = gmpy2.invert(e,phi)

print("N:",N)
print("p:",p)
print("q:",q)
print("e:",e)
print("phi:",phi)
print("d:",d)

r,txt = rsa_conspicuous_check(N,p,q,d,e)
if r == 0:
  print("RSA key has no conspicuousness")
else:
  print("RSA key has Conspicuousness:")
  print(txt)

sys.exit(-1)
