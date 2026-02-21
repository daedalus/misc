#!/usr/bin/env python3
# Author Dario Clavijo 2022

import sys
import os
from binascii import unhexlify

CMD = "/sbin/cryptsetup luksAddKey /dev/sda5 --master-key-file /tmp/master.key"


def main():
    def writefile(filename, data):
        with open(filename, "wb") as fp:
            fp.write(data)

    K = [line.rstrip() for line in open(sys.argv[1])]
    for k1 in K:
        for k2 in K:
            if k1 != k2:
                k = k1 + k2
                data = unhexlify(k)
                print(("k:", k))
                print((len(k), len(data)))
                writefile("/tmp/master.key", data)
                os.system(CMD)


if __name__ == "__main__":
    main()
