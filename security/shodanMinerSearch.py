#!/usr/bin/env python
# Author Dario Clavijo 2018

import shodan
import socket


def sendcommand(ip, port, command):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.sendall(command)
    data = s.recv(1024)
    s.close()
    return data


api = shodan.Shodan(open(".shodan/api_key").read().strip())

result = api.search("cgminer")

for item in result["matches"]:
    ip = item["ip_str"]
    port = item["port"]
    print(ip, port)
    print(sendcommand(ip, port, "summary"))
    print(sendcommand(ip, port, "version"))
