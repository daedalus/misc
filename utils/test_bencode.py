#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bencode
import sys
import json

f = open(sys.argv[1], "r")
raw_data = f.read()
data = bencode.bdecode(raw_data)
# for i in data['info']['pieces'].split(" "):
#    print i.encode("hex")
# print data
print(data)
