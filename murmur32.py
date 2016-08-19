# implementation from the wikipedia page https://en.wikipedia.org/wiki/MurmurHash

rotl = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

def Murmur3_32(key, len, seed):
    # Note: In this version, all integer arithmetic is performed with unsigned 32 bit integers.
    # In the case of overflow, the result is constrained by the application of modulo {\displaystyle 2^{32}} 2^{32} arithmetic.
    
	c1 = 0xcc9e2d51
	c2 = 0x1b873593
	r1 = 15
	r2 = 13
	m = 5
	n = 0xe6546b64
 
    hash = seed

    #for each fourByteChunk of key
    key_list = [key[i:i+4] for i in range(0, len(key), 4)]
    for fourbytechunk in key_list:
	
	if len(fourbytechunk) == 4
        	k = int(fourbytechunk.encode('hex'),16)

        	k = k * c1
        	#k = (k ROL r1)
		k = ROTL(k,r1i,32)
        	k = k * c2

        	hash = hash ^ k
        	#hash = (hash ROL r2)
		hash = ROTL(hash,r2,32)
        	hash = hash * m + n

    	else:
		remainingBytes = int.from_bytes(fourbytechunk.to_bytes(len(fourbytechunk), byteorder='little'), byteorder='big', signed=False)
	        # Note: Endian swapping is only necessary on big-endian machines.
        	#       The purpose is to place the meaningful digits towards the low end of the value,
	        #       so that these digits have the greatest potential to affect the low range digits
        	#       in the subsequent multiplication.  Consider that locating the meaningful digits
	        #       in the high range would produce a greater effect upon the high digits of the
        	#       multiplication, and notably, that such high digits are likely to be discarded
	        #       by the modulo arithmetic under overflow.  We don't want that.
        
        	remainingBytes = remainingBytes * c1
 	       	remainingBytes = ROTL(remainingBytes,r1,32)
        	remainingBytes = remainingBytes * c2

        	hash = hash ^ remainingBytes
 
    	hash = hash ^ len

    hash = hash ^ (hash >> 16)
    hash = hash * 0x85ebca6b
    hash = hash ^ (hash >> 13)
    hash = hash * 0xc2b2ae35
    hash = hash ^ (hash >> 16)
