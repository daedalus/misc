Min = lambda a,b: a * (a < b) + b * (b <= a)
Max = lambda a,b: a * (a > b) + b * (b >= a)

Upper = lambda s: "".join(chr(ord(s[i]) * int(not (s[i] >= 'a' and s[i] <='z')) + (ord(s[i]) - 32) * (s[i] >= 'a' and s[i] <= 'z')) for i in range(0,len(s)))
Lower = lambda s: "".join(chr(ord(s[i]) * int(not (s[i] >= 'A' and s[i] <= 'Z')) + (ord(s[i]) + 32) * (s[i] >= 'A' and s[i] <= 'Z')) for i in range(0,len(s)))

Upper2 = lambda s: "".join(chr(ord(s[i]) - 32 * (s[i] >= 'a' and s[i] <= 'z' )) for i in range(0,len(s)))
Lower2 = lambda s: "".join(chr(ord(s[i]) + 32 * (s[i] >= 'A' and s[i] <= 'Z' )) for i in range(0,len(s)))


def test():
  print(Min(3,10))
  print(Max(3,10))
  print(Upper("dario"))
  print(Upper2("dario"))
  print(Lower("DARIO"))
  print(Lower2("DARIO"))


test()
