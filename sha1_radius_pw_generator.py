#!/usr/bin/env python3
# Autor Dario Clavijo 2023

import hashlib, sys, base64

salt = sys.argv[1].encode("utf-8")
passwd = sys.argv[2].encode("utf-8")

print((base64.b64encode(hashlib.sha1(passwd + salt).digest() + salt).decode("utf8")))
