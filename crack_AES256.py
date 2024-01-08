#!/usr/bin/env python

# -*- coding: utf-8 -*-

import aes
import hashlib
import base64

from Crypto import Random
from Crypto.Cipher import AES


def decrypt(encrypted, passphrase):
    cipher = AES.new(passphrase, AES.MODE_CBC)
    return cipher.decrypt(base64.b64decode(encrypted))


DecodeAES = lambda secret, e: aes.decryptData(secret, base64.b64decode(e))


def sha256(x):
    return hashlib.sha256(x).digest()


def Hash(x):
    if type(x) is str:
        x = x.encode("utf-8")
    return sha256(sha256(x))


def pw_decode(s, password):
    if password is not None:
        secret = Hash(password)
        try:
            d = DecodeAES(secret, s)
            # d = decrypt(s,secret)
        except Exception as e:
            raise Exception("Invalid password")
        return d
    else:
        return s


def try_pw(encoded_seed, pw_cand):
    seed = ""
    try:
        seed = pw_decode(encoded_seed, pw_cand)
    except Exception:
        seed = ""
    finally:
        pass
    return seed


def chk_seed(seed):
    if len(seed) == 0:
        return False
    for cnt, c in enumerate(seed, start=1):
        if cnt > 32:
            return True
        i = ord(c)
        if i < 48:
            return False
        if i > 57:
            if i < 97:
                return False
            if i > 102:
                return False
    return True


def xselections(items, n):
    if n == 0:
        yield []
    else:
        for i in range(len(items)):
            for ss in xselections(items, n - 1):
                yield [items[i]] + ss


# Numbers = 48 - 57
# Capital = 65 - 90
# Lower = 97 - 122
numb = list(range(48, 58))
cap = list(range(65, 91))
low = list(range(97, 123))

choice = 0
# while int(choice) not in range(1,8):
# 		choice = raw_input('''
# 		1) Numbers
# 		2) Capital Letters
# 		3) Lowercase Letters
# 		4) Numbers + Capital Letters
# 		5) Numbers + Lowercase Letters
# 		6) Numbers + Capital Letters + Lowercase Letters
# 		7) Capital Letters + Lowercase Letters
# 		: ''')
#

choice = 3
poss = []
if choice == 1:
    poss += numb
elif choice == 2:
    poss += cap
elif choice == 3:
    poss += low
elif choice == 4:
    poss += numb
    poss += cap
elif choice == 5:
    poss += numb
    poss += low
elif choice == 6:
    poss += cap
    poss += low
    poss += numb
elif choice == 7:
    poss += cap
    poss += low

bigList = [chr(i) for i in poss]
special = False
if special:
    bigList.extend(
        (
            ".",
            " ",
            "_",
            "-",
            "+",
            "/",
            "*",
            "!",
            "?",
            "'",
            '"',
            "#",
            "$",
            "%",
            "(",
            ")",
            "[",
            "]",
            "^",
            "{",
            "}",
            "@",
            ",",
            ";",
            ":",
        )
    )


def test():
    encoded_seed = "Ww9jsiumblVPSM5owcLS6wODqxh0YDLIg/g+mNv+nuNP+f7yyhqOomTlK9tDv8xV0kYt/nUDeTZNtUOr3Zfp2w=="
    # encoded_seed = 'QJA7vVqVDsUM1CaKVJXVSvO0e8hkQUsQbE5YqfguJX3Fs+1WP5XDSAjtxQU5L2fQiS7p5+zJ58B2lftmiZaa5g=='
    # encoded_seed = 'VsIJxlznWkfRauhF6sGvjdZxt3qtWDdVQjbE+KFtKXjarc7IfcJxbWq9LACWVO7t8Rqwp+/OvbJHsxzwZ6Ys8Q=='

    cnt = 0
    cnt_good = 0

    MIN = 1
    MAX = 14
    for i in range(MIN, MAX + 1):
        for s in xselections(bigList, i):
            t = "".join(s)
            pw_cand1 = t
            cnt += 1
            if cnt % 1000 == 0:
                print("trying:", pw_cand1)

            seed = try_pw(encoded_seed, pw_cand1)
            if chk_seed(seed):
                print("pw is good: %s" % pw_cand1)
                print(seed)
                cnt_good += 1
                break

    print("cnt: %d" % cnt)
    print("cnt_good: %d" % cnt_good)


def test1():
    encoded_seed = "Ww9jsiumblVPSM5owcLS6wODqxh0YDLIg/g+mNv+nuNP+f7yyhqOomTlK9tDv8xV0kYt/nUDeTZNtUOr3Zfp2w=="
    seed = try_pw(encoded_seed, "test")
    if chk_seed(seed):
        print("ok")
        print(seed)


test()
