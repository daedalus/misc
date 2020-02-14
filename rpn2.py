#!/usr/bin/env python
# A simple reverse polish notation calculator
# Author Dario Clavijo 2018

r = 0
a = 0
b = 0

import fileinput

debug = False

ops = []
stack = []
for line in fileinput.input():
        line = line.rstrip()
	if line != "":
		ops += line.split(" ")

for op in ops:
	stack.append(op)
	if op == "+":
		a = int(stack[-2])
		b = int(stack[-3])
		r = a + b
		stack.pop()
		stack.pop()
		stack.pop()
		stack.append(r)
                if debug:	
			print r
	if op == "*":
		a = int(stack[-2])
                b = int(stack[-3])
		r = a * b
		stack.pop()
		stack.pop()
		stack.pop()
		stack.append(r)
		if debug:
        		print r
	if op == "-":
	        a = int(stack[-2])
	        b = int(stack[-3])
		stack.pop()
		stack.pop()
		stack.pop()
		r = a - b
        	stack.append(r)
		if debug:
	        	print r
	if op == "/":
		a = int(stack[-2])
               	b = int(stack[-3])
		stack.pop()
       		stack.pop()
               	stack.pop()
		r = a / b
     		stack.append(r)
		if debug:
               		print r
        if op == "%": 
                a = int(stack[-2])
                b = int(stack[-3])
                stack.pop()
                stack.pop()
                stack.pop()
                r = a % b
                stack.append(r)
		if debug:
                	print r
        if op == "**": 
                a = int(stack[-2])
                b = int(stack[-3])
                stack.pop()
                stack.pop()
                stack.pop()
                r = a ** b
                stack.append(r)
		if debug:
                	print r
        if op == "^": 
                a = int(stack[-2])
                b = int(stack[-3])
                stack.pop()
                stack.pop()
                stack.pop()
                r = a ^ b
                stack.append(r)
		if debug:
                	print r
        if op == ">>": 
                a = int(stack[-2])
                b = int(stack[-3])
                stack.pop()
                stack.pop()
                stack.pop()
                r = a >> b
                stack.append(r)
		if debug:
                	print r
        if op == "<<": 
                a = int(stack[-2])
                b = int(stack[-3])
                stack.pop()
                stack.pop()
                stack.pop()
                r = a << b
                stack.append(r)
		if debug:
                	print r

if len(stack) > 1:
	print stack
else:
	print stack[0]
