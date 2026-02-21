#!/usr/bin/env python

fdbuser = '4b5ad6b9623b43a868bb6d15210bb323'

import sys
import requests
import re
import fileinput

def send2db(payload):
  #payload = {'report': str(composite) + '=' + str(factors)}
  data = {'report':payload}

  #print(payload)

  url = 'http://factordb.com/report.php'
  webpage = requests.post(url ,data=data, cookies={'fdbuser': fdbuser}, headers={'User-Agent': 'Mozilla/5.0'}).text
  r = re.findall("Found [0-9]+ factors and [0-9]+ ECM",webpage)
  print(f"Factodb: {str(r)}")
  if r == []:
    print(webpage)
  return(r != None)

limit=10
data = [line.rstrip() for line in fileinput.input()]


def submit(data,limit):
	ret = []
	for x in range(0,len(data),limit):
        	print(x)
		payload = "\n".join(data[x:x+limit])
		if send2db(payload) == False:
        		ret += data[x:x+limit]
	return ret

ret = submit(data,limit)
ret = submit(ret,limit/10)

