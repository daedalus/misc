#!/usr/bin/env python

import urllib.request, urllib.error, urllib.parse
import json
import fileinput


fp = open("/tmp/osget.log", "a")


def get_json(fp, sha256s):
    try:
        url = f"http://www.originstamp.org/api/stamps/{sha256s}"
        request = urllib.request.Request(
            url,
            headers={
                "Authorization": 'Token token="{API_KEY}"',
                "User-Agent": "curl/7.43.0",
                "Content-type": "application/json",
            },
        )
        data = urllib.request.urlopen(request).read()
        fp.write("%s OK\n" % sha256s)
        return json.loads(data)
    except:
        fp.write("%s FAIL\n" % sha256s)
        return


for line in fileinput.input():
    if data := get_json(fp, line.replace("\n", "")):
        print(data["blockchain_transaction"]["private_key"])

fp.close()
