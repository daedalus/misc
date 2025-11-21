import os
import base64
import binascii
from bip_utils import *
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def pipeline(password, mnemonic = None, xprv = None):
    assert not (mnemonic == None and xprv == None)

    salt = b"\xff"*32
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10_000_000,
    )
    key = kdf.derive(password.encode())

    if mnemonic:
        # Generate seed
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate("")
        print("Seed:", seed_bytes.hex())
        # BIP32 master key for Bitcoin (NOT SLIP-0010)
        bip32_mst = Bip32Secp256k1.FromSeed(seed_bytes)
        xprv = bip32_mst.PrivateKey().ToExtended()


    bip32_mst = Bip32Slip10Secp256k1.FromExtendedKey(xprv)

    raw_priv_hex = bip32_mst.PrivateKey().Raw().ToHex()
    chain_code_hex = bip32_mst.PrivateKey().ChainCode().ToHex()

    
    print("Master xprv:", xprv)
    print("Raw priv:", raw_priv_hex)
    print("Chain code:", chain_code_hex)


    a=int(key.hex(),16)
    b=int(chain_code_hex,16) 
    c=int(raw_priv_hex,16)

    A,B = a ^ b, a ^ c

    chain_code_hex = '{:064x}'.format(A)
    raw_priv_hex = '{:064x}'.format(B)

    # Reconstruct manually
    priv_key_bytes = binascii.unhexlify(raw_priv_hex)
    chain_code_bytes = binascii.unhexlify(chain_code_hex)

    # --- VERSION BYTES (4-byte sequences) for Bitcoin mainnet ---
    xpub_ver = b"\x04\x88\xAD\xE4"
    xprv_ver = b"\x04\x88\xB2\x1E"
    net_versions = Bip32KeyNetVersions(xprv_ver, xpub_ver)

    # --- Build Bip32KeyData (master key example: depth=0, index=0, parent fingerprint = 0) ---
    key_data = Bip32KeyData(
        depth=0,
        index=0,
        chain_code=Bip32ChainCode(chain_code_bytes),
        parent_fprint=b"\x00\x00\x00\x00"
    )

    # --- Construct Bip32 object from private key + key_data ---
    bip32 = Bip32Slip10Secp256k1.FromPrivateKey(priv_key_bytes, key_data, net_versions)

    # --- Export extended private/public keys ---
    xprv_rec = bip32.PrivateKey().ToExtended()
    #assert xprv == xprv_rec

    print("Reconstructed xprv:", xprv_rec)

    print("To print: ")
    print("="*30)
    for i in range(6): print(xprv_rec[i*22:(i+1)*22])
    print("="*30)
    return xprv_rec
    
password = "password"

#mnemonic = "panel whisper dutch urge chicken despair ladder together target consider vague robot"
#xprv = "xprv9s21ZrQH143K2vNDXNVDkJFaeR2P8jU4f2H3KDaY9raPytJ9Ht6ru4KZe8JV6DYZcWAU2uWi1psNkx6ZmvZPT6kEKTNBToUi3n8Ry9sL18m"

mnemonic = "panel whisper dutch urge chicken despair ladder together target consider vague robot"
xprv = None
xprv_rec = pipeline(password, mnemonic, xprv)

mnemonic = None
pipeline(password, mnemonic, xprv_rec)

