#!/usr/bin/env python
# Author Dario Clavijo 2018

def split(data):
        mid = int(len(data) / 2)
        return data[:mid],data[mid:]

def partition(n,data):
	if n >0:
        	tmp = []
                for dataset in data:
                	a,b = split(dataset)
                        tmp += [a] + [b]
			print tmp
                return partition(n-1,tmp)
	else:
        	return data

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
print data
p = 3 # partitions will be 2^n
partitions = partition(p,[data]) 
print partitions
