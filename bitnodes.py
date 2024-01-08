#!/usr/bin/env python
import urllib.request, urllib.error, urllib.parse
import json
import sys
import random

url = "https://bitnodes.21.co/api/v1/snapshots/latest/"


def make_request(*args):
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-agent", "Mozilla/5.0" + str(random.randrange(1000000)))]
    try:
        return opener.open(*args).read().strip()
    except Exception as e:
        try:
            p = e.read().strip()
        except:
            p = e
        raise Exception(p)


def getjson(url):
    return json.loads(make_request(url))


data = getjson(url)

for node in data["nodes"]:
    print(node)
