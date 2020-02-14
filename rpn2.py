#!/usr/bin/env python
# A simple reverse polish notation calculator
# Author Dario Clavijo 2018
import fileinput

r = 0
a = 0
b = 0
debug = False

def load_ops(fp):
	ops = []
	for line in fp:
        	line = line.rstrip()
		if line != "":
			ops += line.replace("  "," ").replace("  "," ").split(" ")
	return ops

def proc(ops):
	stack = []
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
                        print stack 
        	        a = int(stack[-3])
        	        b = int(stack[-2])
        	        stack.pop()
        	        stack.pop()
        	        stack.pop()
        	        r = a >> b
                        print r,a,b
                	stack.append(r)
			if debug:
                		print r
        	if op == "<<": 
        	        a = int(stack[-3])
        	        b = int(stack[-2])
        	        stack.pop()
        	        stack.pop()
        	        stack.pop()
               	 	r = a << b
                	stack.append(r)
			if debug:
                		print r
	return stack

ops = load_ops(fileinput.input())
if debug:
	print (ops)
stack = proc(ops)

if len(stack) > 1:
	print stack
else:
	print stack[0]
