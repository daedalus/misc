def swap(S,i,j):
	S[i], S[j] = S[j], S[i]
	return S

def KSA(key):
	S = range(256) # Initialize state array with values 0 .. 255
    	j = 0
    	for i in range(256):
        	j = (j + S[i] + ord(key[i % len(key)])) & 0xFF
        	S = swap(S,i,j)
	return S

def PRGA(S):
  	i = j = 0
    	while True:
        	i = (i + 1) & 0xFF
        	j = (j + S[i]) & 0xFF
       	 	S = swap(S,i,j)
        	yield S[(S[i] + S[j]) & 0xFF]

def keystream(key):
    """Generates an RC4 keystream for the given key."""
    S = KSA(key)
    return PRGA(S)
  

ks = keystream("hola man")
for k in ks:
    print kdef swap(S,i,j):
	S[i], S[j] = S[j], S[i]
	return S

def KSA(key):
	S = range(256) # Initialize state array with values 0 .. 255
    	j = 0
    	for i in range(256):
        	j = (j + S[i] + ord(key[i % len(key)])) & 0xFF
        	S = swap(S,i,j)
	return S

def PRGA(S):
  	i = j = 0
    	while True:
        	i = (i + 1) & 0xFF
        	j = (j + S[i]) & 0xFF
       	 	S = swap(S,i,j)
        	yield S[(S[i] + S[j]) & 0xFF]

def keystream(key):
    """Generates an RC4 keystream for the given key."""
    S = KSA(key)
    return PRGA(S)
  

ks = keystream("hola man")
for k in ks:
    print k
