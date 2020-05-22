#!/usr/bin/env python
# Author Dario Clavijo 2020
# GPlv3
# a factordb number scraper

import urllib3
import sys

t=4
maxdig = 78
perpage = 5000

http = urllib3.PoolManager()

def download(url):
    #global gcontext
    global http
    #req = urllib3.Request(url)
    #data = urllib3.urlopen(req, context=gcontext).read()
    #data = http.request('GET', url).data.decode('utf-8')
    data = http.request('GET', url).data.decode('utf-8')
    
    return data

for digits in range(19,maxdig):
  x = 0
  C = True
  last_data = ""
  while C:
    start = x*perpage
    url = "http://factordb.com/listtype.php?t=%d&mindig=%d&perpage=%d&start=%d&download=1" % (t,digits,perpage,start)
    sys.stderr.write("Downloading: %s\n" % url)
    data = download(url)
    #sys.stdout.write("%s\n" % data.replace("\\n","\n"))
    sys.stdout.write("%s\n" % data)
    sys.stderr.flush()
    C = (data != last_data)
    last_data = data
    sys.stdout.flush()
    x +=1
