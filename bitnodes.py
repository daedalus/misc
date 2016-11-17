#!/usr/bin/env python
import urllib2
import json
import sys
import random

url = "https://bitnodes.21.co/api/v1/snapshots/latest/"

def make_request(*args):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0'+str(random.randrange(1000000)))]
    try:
        return opener.open(*args).read().strip()
    except Exception,e:
        try: p = e.read().strip()
        except: p = e
        raise Exception(p)

def getjson(url):
	jdata = json.loads(make_request(url))
	return jdata

data = getjson(url)

for node in data['nodes']:
	print node
