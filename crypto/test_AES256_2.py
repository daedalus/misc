from Crypto import Random
from Crypto.Cipher import AES
import base64
import random
import hashlib
import binascii

random.seed(1)

BLOCK_SIZE = 16


def encrypt(message, passphrase):
    # passphrase MUST be 16, 24 or 32 bytes long, how can I do that ?
    # IV = Random.new().read(BLOCK_SIZE)
    # print IV
    aes = AES.new(passphrase, AES.MODE_ECB)
    return base64.b64encode(aes.encrypt(message))


def decrypt(encrypted, passphrase):
    # IV = Random.new().read(BLOCK_SIZE)
    # print IV
    aes = AES.new(passphrase, AES.MODE_ECB)
    return aes.decrypt(base64.b64decode(encrypted))


def sha256(string):
    return hashlib.sha256(string).digest()


def getpw():
    while True:
        passphrase = (
            hex(random.getrandbits(32)).replace("0x", "").replace("L", "").zfill(16)
        )
        if binascii.hexlify(sha256(passphrase)) == sha256_pass_check:
            break
    return passphrase


sha256_pass_check = "b0676958f7d5ced730621c30299e40801b088d9d2df5d0425944f12ed5c58404"
sha256_payload_check = (
    "2634454f86004e399ccc074e27f9b34ac96c60c7cfbe23a7c42ff97c994cd684"
)

str_payload = "This is a message               "


def test1(string):
    passphrase = (
        hex(random.getrandbits(32)).replace("0x", "").replace("L", "").zfill(16)
    )

    print(len(passphrase), passphrase)
    print(binascii.hexlify(sha256(string)).zfill(64))
    print(binascii.hexlify(sha256(passphrase)).zfill(64))

    return encrypt(string, passphrase)


def test2(payload):
    passphrase = getpw()
    print(passphrase)
    dec = decrypt(payload, passphrase)
    # print dec
    return dec if binascii.hexlify(sha256(dec)) == sha256_payload_check else False


def main():
    # u = test1(str_payload)
    u = "N8WjTJKAcE4Z3fI6Ozx6sI97ZGvWF5e7R2jjg7Nw90s="
    print(u)
    d = test2(u)
    print(d)


main()
