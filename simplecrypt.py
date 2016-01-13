#!/usr/bin/env python
# Author Dario Clavijo 2016

import binascii
import hashlib

MAX_STRETCH = 1000

def bin_sha256(tmp):
	h = hashlib.new('sha256')
	h.update(tmp)
	#return h.hexdigest().zfill(64).decode('hex')
	return h.digest()

def stretch_password(password):
	tmp = bin_sha256(password)
	for i in range(MAX_STRETCH):
		tmp = bin_sha256(tmp)
	return tmp

def decrypt(txt,password):
	return crypt(txt.decode('base64').decode('hex'),password).decode('base64').decode('hex')
	
def crypt(txt,password):
	a = int(txt.encode('hex'),16)
	b = int(stretch_password(password).encode('hex').zfill(64),16)
	return hex(a ^ b).replace('0x','L').replace('L','').encode('base64').replace('\n','')


def test():
	print 'crypt: ',crypt('abcd','1234')
	print 'decrypt: ', decrypt('N2Y1ZGU1M2I0MjFkZDExMGJjMWVjYjJhZWJiMjQxYWQwNTA0NjQxNjg4YTg5YTg4ZTI0NmY4MmJjMDRjMTY0OA==','1234')

test()
