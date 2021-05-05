#!/usr/bin/env python
# Author Dario Clavijo 2018
# ssh id_rsa.pub field decoder
import sys
import os

if len(sys.argv) > 1:
    fp = open(sys.argv[1])
else:
    fp = open(os.getenv("HOME") + "/.ssh/id_rsa.pub")

for line in fp:
    line = line.rstrip()
    a = line.split(" ")
    if a[0] == "ssh-rsa":
        print "Base64:", a[1]
        print "=" * 128
        bindata = a[1].decode("base64")

        def getdata(start, end):
            field = bindata[start:end]
            if len(field) > 0:
                pos = int(field.encode("hex"), 16)
                data = bindata[end : end + pos]
            else:
                pos = len(bindata)
                data = None
            return pos, data

        start = 0
        end = 4
        pos = 0
        c = []
        data = ""
        while pos < len(bindata):
            pos, data = getdata(start, end)
            if data != None:
                print "%d,%d,%d,%s" % (start, end, pos, data.encode("hex"))
                c.append(data)
            start += pos + 4
            end = start + 4

        print "=" * 128
        print "Key type:", c[0]
        print "Public exponent:", int(c[1].encode("hex"), 16)
        print "Modulus bits:", (len(c[2]) - 1) * 8
        print "Modulus:", int(c[2].encode("hex"), 16)
