#!/usr/bin/env python
# A simple and encrypted password cache in less than 100 sloc. 
# Author Dario Clavijo 2019
# GPLv3

import hashlib
import getpass
import os
import sys
import pwd
import datetime
import base64

from pymemcache.client import base

from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE=16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE) 
unpad = lambda s : s[0:-ord(s[-1])]

# AES encryption: (plaintext -> decrypted)
def encrypt(message, passphrase):
    # passphrase MUST be 16, 24 or 32 bytes long, how can I do that ?
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return base64.b64encode(IV) + " " +  base64.b64encode(aes.encrypt(message))

# AES decryption (crypted -> plaintext)
def decrypt(encrypted, passphrase, IV = None):
    if IV == None:
        IV = Random.new().read(BLOCK_SIZE)
    else:
        IV = base64.b64decode(IV)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return aes.decrypt(base64.b64decode(encrypted))

# simple sha256 hash(input) -> hex
def sha256hex(s):
    return hashlib.sha256(s).hexdigest()

client = base.Client(('localhost', 11211))

# here we get a key from memcached
def getmemcached(key):
	try:
		s = client.get(key)
		return s
	except:
		return None

def setmemcached(key,value):
	client.set(key,value,expire=7200)

# this funcion generates a temporary key for encrypting our password
def getkey():
    salt = "salt"
    username = pwd.getpwuid(os.getuid()).pw_name
    host = os.uname()[1]
    date = datetime.datetime.now().strftime("%m/%d/%Y, %H")
    key = sha256hex(salt + username + host + date)
    return key    

# this is the main funcion were we encrypt and rencrypt our password at every iteration
# memcached_encrypted(key_s0) -> decrypted(key_s0) -> encrypted(key_s1) -> memcached_encrypted(key_s1)

def pw_get():
    key = getkey()
    print key,len(key[0:32]),len(key[32:65])
    s = getmemcached(key[0:32])
    if s != None:
        sys.stderr.write("memcached Crypted: " + s + "\n")
        s = s.split(" ")
        ret = unpad(decrypt(s[1],key[32:65],s[0]))
        key = getkey()
        sys.stderr.write("Time key: "+ key + "\n")
        s = encrypt(pad(ret),key[32:65])
        sys.stderr.write("reCrypted: " + s + "\n")
        setmemcached(key[0:32],s)
        return ret
    else:
        pw0 = getpass.getpass("Password: ")
        pw1 = getpass.getpass("Retype password: ")
        if pw0 == pw1:
            key = getkey()
            sys.stderr.write("Time key: "+ key + "\n")
            s = encrypt(pad(pw0),key[32:65])
            sys.stderr.write("Crypted: "+ s + "\n")
            setmemcached(key[0:32],s)
            del pw1
            return pw0


print pw_get()
