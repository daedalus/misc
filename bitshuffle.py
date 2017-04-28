import numpy

def bintobit(tmp):
	tmp = numpy.frombuffer(tmp,dtype=numpy.uint8)
        tmp = numpy.unpackbits(tmp)
	return tmp

def Transpose8X8(tmp):
	tmp = bintobit(tmp)
	tmp = numpy.reshape(tmp,(8,8))
	tmp = numpy.reshape(tmp.T,(1,64))
	tmp = numpy.packbits(tmp)
	return tmp.tobytes()

def bitshuffle(buff):
	if len(buff) % 8 == 0:
		buff2 = ""
		for i in xrange(0,len(buff)-1,8):
			buff2 += Transpose8X8(buff[i:i+8])
		return buff2
	else:
		raise Exception ('Buffer must be a multiple of 8 bytes')


if __name__ == "__main__":
	a = "Dario Clavijo   "
	print a,len(a)
	print a.encode('hex')		
	print bintobit(a)

	a = bitshuffle(a)
	print a.encode('hex')
	print bintobit(a)
	print bitshuffle(a)

