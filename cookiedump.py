#!/usr/bin/env python
import os
import sqlite3
import pwd
import sys


def getFromCookieDB(filename):
    connection = sqlite3.connect(filename)
    cur = connection.cursor()
    cur.execute("SELECT * FROM cookies")
    rows = cur.fetchall()
    for row in rows:
        print row


def dump(uid):
    try:
        filename = os.path.join(
            pwd.getpwuid(uid).pw_dir, ".config/chromium/Default/Cookies"
        )
    except:
        filename = ""
    if filename != "" and os.path.isfile(filename):
        getFromCookieDB(filename)


if len(sys.argv) > 1:
    dump(int(sys.argv[1]))
else:
    for u in pwd.getpwall():
        dump(u.pw_uid)
