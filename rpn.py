#!/usr/bin/env python
# A simple reverse polish notation calculator
# Author Dario Clavijo 2018

r = 0
a = 0
b = 0

stack = []
while True:
    ops = str(raw_input(">"))
    if ops != "":
        ops = ops.split()
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
                print r
            if op == "*":
                a = int(stack[-2])
                b = int(stack[-3])
                r = a * b
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(r)
                print r
            if op == "-":
                a = int(stack[-2])
                b = int(stack[-3])
                stack.pop()
                stack.pop()
                stack.pop()
                r = a - b
                stack.append(r)
                print r
            if op == "/":
                a = int(stack[-2])
                b = int(stack[-3])
                stack.pop()
                stack.pop()
                stack.pop()
                r = a / b
                stack.append(r)
                print r
        print stack
