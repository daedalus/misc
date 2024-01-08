#!/usr/bin/env python
#
# Android FDE Decryption
#
# Authors:  Thomas Cannon <tcannon@viaforensics.com>
#           Andrey Belenko <abelenko@viaforensics.com>
# Requires: Python, M2Crypto (sudo apt-get install python-m2crypto)
#
# Parses the header for the encrypted userdata partition.
# Decrypts the master key found in the header using a supplied password
# Decrypts the first sector of an encrypted userdata partition using the decrypted key
# Written for Nexus S (crespo) running Android 4.0.4
# Header is located in file userdata_footer on the efs partit

from os import path
from M2Crypto import EVP
import hashlib
import struct
import sys

# Inputs
header_file = sys.argv[1]
encrypted_partition = sys.argv[2]
password = sys.argv[3]

HEADER_FORMAT = "=LHHLLLLLLL64s"  # Taken from cryptfs.h in crespo source.
HASH_COUNT = 2000
KEY_LEN_BYTES = 16
IV_LEN_BYTES = 16
SECTOR_SIZE = 512
BLOCK_SIZE = 16
SECTOR_OFFSET = 0
ENCRYPT = 1
DECRYPT = 0

assert path.isfile(header_file), "Input file '%s' not found." % header_file
assert path.isfile(encrypted_partition), (
    "Input file '%s' not found." % encrypted_partition
)
header = open(header_file, "rb").read()

# Unpack header
(
    ftrMagic,
    majorVersion,
    minorVersion,
    ftrSize,
    flags,
    keySize,
    spare1,
    fsSize1,
    fsSize2,
    failedDecrypt,
    cryptoType,
) = struct.unpack(HEADER_FORMAT, header[0:100])

encrypted_key = header[ftrSize : ftrSize + keySize]
salt = header[ftrSize + keySize + 32 : ftrSize + keySize + 32 + 16]

pbkdf2 = EVP.pbkdf2(
    password, salt, iter=HASH_COUNT, keylen=KEY_LEN_BYTES + IV_LEN_BYTES
)
key = pbkdf2[:KEY_LEN_BYTES]
iv = pbkdf2[KEY_LEN_BYTES:]

# Decrypt the encryption key
cipher = EVP.Cipher(alg="aes_128_cbc", key=key, iv=iv, padding=0, op=DECRYPT)
decrypted_key = cipher.update(encrypted_key)
decrypted_key = decrypted_key + cipher.final()

print(decrypted_key.encode("hex"))
