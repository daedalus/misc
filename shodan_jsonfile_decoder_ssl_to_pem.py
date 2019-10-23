#!/usr/bin/env python
# Author Dario Clavijo 2019
# GPLv3

import json
import sys
import gzip

data = gzip.open(sys.argv[1],"r").read()
for line in data.split("\n"):
        #print(line)
	try:
		reg = json.loads(line)
	except:
		reg = None
	if reg:
        	try:
        		asn = reg['asn'] 
		except:	
			asn = ""
        	a = reg['hostnames']
        	if len(a) > 0:
        		a = "_".join(a)
        	else:
        	        a = ""
        	b = reg['domains']
        	if len(b) > 0:
        	        b = "_".join(b)
        	else: 
        	        b = ""
        	h = "%s_%s_%s_%s" % (asn,reg['ip_str'],a,b)
		h = h.replace("__","")
		#print h
		cert = reg['ssl']['chain']
		bits = reg['ssl']['cipher']['bits']
		fp = open(sys.argv[2] + h + "_%dbits.pem" % bits,"w")
		for line in cert:
			fp.write(line)
		fp.close()
