#!/usr/bin/env python
# autor Dario Clavijo 2017

import subprocess

def ifUpDown(iface):
	subprocess.call(['ifconfig',iface,'down'])
	subprocess.call(['ifconfig',iface,'up'])

def ifUp(iface):
	subprocess.call(['ifconfig',iface,'up'])

def ifDown(iface):
	subprocess.call(['ifconfig',iface,'down'])

def setMonitorMode(iface):
	subprocess.call(["ifconfig",iface,"down"])
	subprocess.call(["iwconfig",iface,"mode","monitor"])
	subprocess.call(["ifconfig",iface,"up"])

def setManagedMode(iface):
	subprocess.call(['ifconfig',iface,'down'])
	subprocess.call(['iwconfig',iface,'mode','managed'])
	subprocess.call(['ifconfig',iface,'up'])

def wifiJoin(iface,essid):
	subprocess.call(['dhclient','-v -r'])
	subprocess.call(['killall','dhclient'])
	subprocess.call(['iwconfig',iface,'essid',essid])
	subprocess.call(['dhclient','-v',iface])

def setIpAddress(iface,ipaddr,netmask):
	subprocess.call(['ifconfig', iface, ipaddr, 'netmask', netmask])

def setPromisc(iface):
	subprocess.call(['ifconfig', iface,'promisc'])

def unsetPromisc(iface):
	subprocess.call(['ifconfig', iface,'-promisc'])

def setMtu(iface,mtu):
	subprocess.call(['ifconfig',iface,int(mtu)])

def setHWAddr(iface,hwAddr):
	subprocess.call(['ifconfig','iface','hw ether',hwaddr])


