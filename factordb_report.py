#!/usr/bin/env python

fdbuser = '4b5ad6b9623b43a868bb6d15210bb323'

import sys
import requests
import re

def send2db(payload):
  #payload = {'report': str(composite) + '=' + str(factors)}
  data = {'report':payload}
  url = 'http://factordb.com/report.php'
  webpage = requests.post(url ,data=data, cookies={'fdbuser': fdbuser}, headers={'User-Agent': 'Mozilla/5.0'}).text
  print("Factodb: " + re.findall("Found [0-9] factors and [0-9] ECM",webpage)[0])


limit=100
data=[]
fp=open(sys.argv[1])
for line in fp:
	data.append(line.rstrip())

for x in range(0,len(data),limit):
	payload = data[x:x+limit]
	send2db(payload)
