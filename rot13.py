#!/usr/bin/env python
# Author Dario Clavijo 2016
# simple ROT13 algo or Caesar Cipher


def ROT13(message):
    p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    r = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM "
    return "".join([r[p.find(c)] for c in message])


if __name__ == '__main__':
  message = "Dario Clavijo"
  assert ROT13(ROT13(message)) == message
