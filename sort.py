#!/usr/bin/env python

import random

numbers = [6,5,3,4,2,7,8,1,9,11,10]

def bubblesort(numberset):
	for j in xrange(len(numberset)-1):
		for i in xrange(len(numberset)-1):
			if numberset[i] > numberset[i+1]:
		 		numberset[i],numberset[i+1] = numberset[i+1],numberset[i]		
	return numberset

def swap(a,b): return b,a 

def partition(A, lo, hi):
	pivot = A[hi]
	i = lo     #place for swapping
	for j in (lo, hi – 1):
		if A[j] <= pivot:
       			A[i],A[j] = swap (A[i],A[j])
			i := i + 1
    	A[i], A[hi] = swap (A[i], A[hi])
	return i

def quicksort(A, lo, hi):
	if lo < hi:
		p = partition(A, lo, hi)
        	quicksort(A, lo, p – 1)
        	quicksort(A, p + 1, hi)

print numbers
print bubblesort(numbers)
print quicksort(numbers,0,len(numbers))
