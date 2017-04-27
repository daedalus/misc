import bitshuffle
import fileinput
import numpy

def buff_shuffle(buff):
	print  len(buff)
        buff = numpy.frombuffer(buff, dtype='S1')
        buff = bitshuffle.bitshuffle(buff).tostring()
        return buff

data = ""
for line in fileinput.input():
	data += line

print buff_shuffle(data)
