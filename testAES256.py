from Crypto import Random
from Crypto.Cipher import AES
import base64
import hashlib

BLOCK_SIZE=16

# MODES CFB,CBC XTS
 

def encrypt(message, passphrase,mode):
    # passphrase MUST be 16, 24 or 32 bytes long, how can I do that ?
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, mode, IV)
    return base64.b64encode(IV),base64.b64encode(aes.encrypt(message))

def decrypt(encrypted, passphrase,mode,IV):
    #IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, mode, base64.b64decode(IV))
    return aes.decrypt(base64.b64decode(encrypted))


def makekey(password):
	return hashlib.sha256(hashlib.sha256(password).digest()).digest()

print 'password = a'

key = makekey('a')

print 'key = double hashed password =',key.encode('hex')

input_str = '0123456789ABCDEF0123456789ABCDEF'

print "input message =",input_str

mode = AES.MODE_CBC

print "MODE = ", mode

IV,enc = encrypt(input_str,key,mode)
print 'IV =',IV,',encrypted message =',enc

dec = decrypt(enc,key,mode,IV)
print "decrypted message = ",dec
