IsEven = lambda a: (a & 1) ^ 1
IsOdd = lambda a: a & 1

MinZeroAnd = lambda a: a * (a <= 0) + 0 * (a > 0)
MaxZeroAnd = lambda a: a * (a >= 0) + 0 * (a < 0)

Sgn = lambda a: (a > 0) - (a < 0) 
Abs = lambda a: a * (a > 0) + (-a) * (a <= 0)

Min = lambda a,b: a * (a < b) + b * (b <= a)
Max = lambda a,b: a * (a > b) + b * (b >= a)

Upper = lambda s: "".join(chr(ord(s[i]) * int(not (s[i] >= 'a' and s[i] <='z')) + (ord(s[i]) - 32) * (s[i] >= 'a' and s[i] <= 'z')) for i in range(0,len(s)))
Lower = lambda s: "".join(chr(ord(s[i]) * int(not (s[i] >= 'A' and s[i] <= 'Z')) + (ord(s[i]) + 32) * (s[i] >= 'A' and s[i] <= 'Z')) for i in range(0,len(s)))

Upper2 = lambda s: "".join(chr(ord(s[i]) - 32 * (s[i] >= 'a' and s[i] <= 'z' )) for i in range(0,len(s)))
Lower2 = lambda s: "".join(chr(ord(s[i]) + 32 * (s[i] >= 'A' and s[i] <= 'Z' )) for i in range(0,len(s)))

clamp = lambda x, min_,max_: min(max(x, min_), max_)


def stringcompare(a,b):
  tmp = 0
  for i in range(0, len(a)):
    tmp += a[i] != b[i]
  return tmp == 0


def lowerbound(x, t):
  #base = t
  #l = len(t)
  #while(l > 1):
  #  half = l >> 1
  #  base += (base[half -1] < x) * half
  #  l -= half
  #return base
  k = 1
  l = len(t)
  while k <= l:
    #print(t[k])
    k = (k << 1) + (t[k] < x)
  #return k.bit_count(),k
  #k >>= k.bit_count()
  #print(bin(k))
  #return t[k]
  #return k.bit_count()
  return k

def test():
  assert(IsOdd(3) == True)
  assert(IsOdd(2) == False)
  assert(IsEven(3) == False)
  assert(IsEven(2) == True)

  assert(MinZeroAnd(-3) == -3)
  assert(MinZeroAnd(3) == 0)
  assert(MaxZeroAnd(-3) == 0)
  assert(MaxZeroAnd(3) == 3)

  assert(Sgn(-3) == -1)
  assert(Sgn(3) == 1)
  assert(Abs(-3) == 3)
  assert(Abs(3) == 3)
  assert(Min(3,10) == 3)
  assert(Max(3,10) == 10)
  assert(Upper("dario"))
  assert(Upper2("dario"))
  assert(Lower("DARIO"))
  assert(Lower2("DARIO"))
  assert(stringcompare("dario","dario") == True)
  assert(stringcompare("dario","dariO") == False)
  assert(clamp(4,10,15) == 10)
  assert(clamp(14,10,15) == 14)
  assert(clamp(24,10,15) == 15)


test()

for i in range(0, 10):
  k = lowerbound(i,[0,1,2,3,4,5,6,7,8,9])
  print(i, k, k.bit_count())

print(lowerbound(5,[6, 3, 7, 1, 5, 8, 9, 0, 2, 4]))

