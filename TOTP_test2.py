#!/usr/bin/env python
# Author Dario Clavijo 2017
# GPLv3

# This programs uses the google authenticator sqlite3 database
import qrcode
import pyotp
import sqlite3
import sys
import os
import tempfile

# mp = tempfile.mkstemp()[1]

# os.system('cat %s | gpg --decrypt > %s' % (sys.argv[1],tmp))

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

for row in c.execute("select * from accounts"):

    account = row[1]
    secret = row[2]
    issuer = row[6]

    data = "otpauth://totp/%s?secret=%s&issuer=%s" % (account, secret, issuer)
    img = qrcode.make(data)
    img.show()
