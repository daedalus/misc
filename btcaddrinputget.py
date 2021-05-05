import urllib2
import json
import sys


def getinputs(addr_test, offset):
    req = urllib2.Request(
        "https://blockchain.info/address/%s?format=json&offset=%d" % (addr_test, offset)
    )
    f = urllib2.urlopen(req)

    data = ""
    addrs = []

    for line in f:
        data += line

    json_obj = json.loads(data)

    for item in json_obj["txs"]:
        for input in item["inputs"]:
            addr = input["prev_out"]["addr"]
            if addr != addr_test:
                addrs.append(addr)

    addrs = sorted(set(addrs))
    return addrs


for i in range(0, 800):
    for addr in getinputs(sys.argv[1], i * 50):
        print addr
