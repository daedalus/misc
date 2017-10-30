#!/usr/bin/env python
# Author Dario Clavijo 2016
# GPLv3

from ftplib import FTP
import sys


USER='test'
PASS='test'
timeout=3

run=True

def upload(ip,filename):
	print "put",filename,ip
	if run:
		ftp = FTP(ip,USER,PASS,timeout=timeout)
		#tp.login()
		ftp.storlines('STOR %s' % filename, open(filename, 'r'))


filename = sys.argv[1]

iprange = sys.argv[2].split(" ")

if len(iprange) > 1:

	j = iprange[0].split(".")
	k = iprange[1].split(".")

	#print a,b


	for a in range(int(j[0]),(int(k[0])+1)):
		for b in range(int(j[1]),int(k[1])+1):
			for c in range(int(j[2]),int(k[2])+1):
				for d in range(int(j[3]),int(k[3])+1):
					ipaddr = str(a) + "." + str(b) + "." + str(c)  + "." + str(d)
					upload(ipaddr,filename)

else:
	upload(iprange[0],filename)
