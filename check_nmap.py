#!/usr/bin/env python
# Author Dario Clavijo 2019
# GPLv3

import sys
import nmap
import json
import socket

nm = None
old_nm = None

status = {0: "OK", 1: "WARNING", 2: "CRITICAL", 3: "UNKNOWN"}


def loadfile(f):
    with open(f, "r") as fp:
        d = fp.read()
    return d


def savefile(f, data):
    with open(f, "w") as fp:
        fp.write(data)


def json2file(f, s):
    json_data = json.dumps(s)
    savefile(f, json_data)


def file2json(f):
    data = loadfile(f)
    return json.loads(data)


host = sys.argv[1]


def getold_nm(host):
    try:
        old_nm = file2json(f".check_nmap.py.{host}.cache")
    except:
        old_nm = None
    return old_nm


def getstate(nm, old_nm, host, port):
    try:
        a = old_nm["tcp"][str(port)]["state"]
    except:
        a = None
    try:
        b = nm[host]["tcp"][port]["state"]
    except:
        b = None
    # print a,b
    return a, b


def getports(nm, host):
    try:
        ports = list(nm[host]["tcp"].keys())
    except:
        ports = []
    return ports


def proc_results(nm, old_nm, host, ports):
    num_status = 0
    output = ""
    output0 = ""
    # print ports
    if len(ports) > 0:
        for port in ports:
            a, b = getstate(nm, old_nm, host, port)
            if a != b:
                output += "tcp port: %s, old_state: %s,  state: %s\n" % (port, a, b)
                num_status = 2
                output0 += f"tcp {port}: {b},"
    else:
        num_status = 3
        output = "Could not get scan results, check your firewall!"

    if num_status == 0:
        output = "No new ports open\n"
    return num_status, output + "\n" + output


def main():
    host = socket.gethostbyname(sys.argv[1])
    old_nm = getold_nm(host)
    nm = nmap.PortScanner()
    nm.scan(host, sys.argv[2], arguments="--system-dns")
    ports = getports(nm, host)
    num_status, output = proc_results(nm, old_nm, host, ports)
    json2file(".check_nmap.py." + host + ".cache", nm[host])
    print(status[num_status] + ": " + output)
    sys.exit(num_status)


main()
