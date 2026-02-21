#!/usr/bin/env python
# Author Dario Clavijo 2020
# Get ssl certificates from most common ports

import sys
import ssl

ssl.DEFAULT_CIPHERS = "ALL"
ports = [25, 261, 443, 448, 465, 563, 587, 614, 636, 686, 989, 990, 993, 994, 995, 3389]

import fileinput

for line in fileinput.input():
    hostname = line.rstrip()
    for port in ports:
        print(f"{hostname}:{str(port)}")
        try:
            pem = ssl.get_server_certificate((hostname, port))
            if pem != None:
                print(pem)
                with open("output/%s_%d.pem" % (hostname, port), "w") as fp:
                    fp.write(pem + "\n")
        except:
            print(f"{hostname} error")
