
#!/usr/bin/env python
# Author Dario Clavijo 2016
# GPLv3
# don't know if the theory is right

a = [0.0,1.0,0.0,1.0]
b = [0.0,0.0,1.0,1.0]
aANDb = [0,0,0,1]
aORb = [0,1,1,1]
aXORb = [0,1,1,0]

#def f(p,q):	
#	return (p*q) / ((p*q) + (1-p)*(1-q))

def stochastic_average_fAND(p,q):
	return (p*q) / 2

def stochastic_average_fOR(p,q):
	return (p+q) / 2

def stochastic_average_fXOR(p,q):
	return ((p-q)*(p-q))/2


def AND(p,q):
	return float(stochastic_average_fAND(p,q) > 0)

def OR(p,q):
	return float(stochastic_average_fOR(p,q) > 0)

def XOR(p,q):
	return float(stochastic_average_fXOR(p,q) > 0)

print "a\tb\tand\tor\txor"
for i in range(0,4):
	print a[i],b[i],stochastic_average_fAND(a[i],b[i]),stochastic_average_fOR(a[i],b[i]),stochastic_average_fXOR(a[i],b[i])

print "a\tb\tand\tor\txor"
for i in range(0,4):
	print a[i],b[i],AND(a[i],b[i]),OR(a[i],b[i]),XOR(a[i],b[i])




