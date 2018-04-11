#!/usr/bin/env python
# Author Dario Clavijo 2018

import os
import urllib2
import json
import ssl
import fileinput
import sys

def get_data(url):
	req = urllib2.Request(url)
	res = urllib2.urlopen(req,timeout=2)
	return res.read()

fp = open(sys.argv[1])
for line in fp:
    url = line.rstrip() + "?info_hash=" + sys.argv[2] + ".lower()
    try:
        print url,get_data(url) 
    except:
        print url,'Error'
