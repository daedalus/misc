#!/usr/bin/env python
# Author Dario Clavijo 2017
# GPLv3

import pyotp
import sqlite3
import sys
import os
import tempfile

tmp = tempfile.mkstemp()[1]

os.system('cat %s | gpg --decrypt > %s' % (sys.argv[1],tmp))

conn = sqlite3.connect(tmp)
c = conn.cursor()

for row in c.execute("select * from accounts"):
	totp=pyotp.TOTP(row[2])
	print totp.now(),row[1]

os.system('shred %s -v' % tmp)
os.system('rm %s' % tmp)
