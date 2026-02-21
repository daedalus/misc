#!/usr/bin/env python
# Author Dario Clavijo 2017
# GPLv3

# This programs uses the google authenticator sqlite3 database

import pyotp
import sqlite3
import sys
import os
import tempfile

tmp = tempfile.mkstemp()[1]

os.system(f"cat {sys.argv[1]} | gpg --decrypt > {tmp}")

conn = sqlite3.connect(tmp)
c = conn.cursor()

for row in c.execute("select * from accounts"):
    totp = pyotp.TOTP(row[2])
    print(totp.now(), row[1])

os.system(f"shred {tmp} -v")
os.system(f"rm {tmp}")
