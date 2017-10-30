#!/usr/bin/env python
# Author Dario Clavijo 2016

import zlib
import bz2
import fileinput
import struct

zlib_magic = 'ZLIB'

def ser_uint(i):
        return hex(i).replace('0x','').replace('L','').zfill(8).decode('hex')
def deser_uint(s):
        return int(s.encode('hex'),16)

def test(msg_data):

        print "Criginal data:",msg_data

        msg_data = zlib.compress(msg_data,1)

        print "Compressed data(hex): " + msg_data.encode('hex')

        msg_data = struct.pack('>4si{0:d}s'.format(len(msg_data))  ,zlib_magic,len(msg_data),msg_data)
        #msg_data = "ZLIB%s%s" % (ser_uint(len(msg_data)),msg_data)

        print "Packed data: " + msg_data.encode('hex')

        if msg_data[:4] == zlib_magic:
                msg_len = deser_uint(msg_data[4:8])
                print "msg_len: {0!s}".format(msg_len)
          
                a,b,c = struct.unpack('>4si{0:d}s'.format(msg_len),msg_data)
                print "Pack:",a,b,c.encode('hex')
                new_data = zlib.decompress(c)
                print "Decompressed data: " + new_data

test('dario')

