#!/usr/bin/env python
# Author Dario Clavijo 2016
# simple ROT13 algo or Caesar Cipher


def rot13(message):
    p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    r = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM "
    return "".join([r[p.find(c)] for c in message])


print rot13(rot13("Dario Clavijo"))
