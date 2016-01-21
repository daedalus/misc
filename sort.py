#!/usr/bin/env python

import random

numbers = [6,5,3,4,2,7,8,1,9,11,10]

def bubblesort(numberset):
	for j in xrange(len(numberset)-1):
		for i in xrange(len(numberset)-1):
			if numberset[i] > numberset[i+1]:
		 		numberset[i],numberset[i+1] = numberset[i+1],numberset[i]		
	return numberset


print numbers
print bubblesort(numbers)
