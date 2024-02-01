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


test()
