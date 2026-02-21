#!/usr/bin/env python
# Arithmetric representation of boolean functions
# Author Dario Clavijo 2019
# The math will always work for input domain [0,1]


def AND(a, b):
    print("AND", a, b)
    return a * b


def XOR(a, b):
    print("XOR", a, b)
    return abs(a - b)


def NOT(a):
    print("NOT", a)
    return XOR(1, a)


def OR(a, b):
    print("OR", a, b)
    return XOR(a, b) + AND(a, b)


def NOR(a, b):
    print("NOR", a, b)
    return XOR(1, (XOR(a, b) + AND(a, b)))


def NAND(a, b):
    print("NAND", a, b)
    return XOR(1, (AND(a, b)))


print("----------")
print(NOT(0))
print(NOT(1))
print("----------")
print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))
print("----------")
print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))
print("----------")
print(OR(0, 0))
print(OR(0, 1))
print(OR(1, 0))
print(OR(1, 1))
print("----------")
print(NOR(0, 0))
print(NOR(0, 1))
print(NOR(1, 0))
print(NOR(1, 1))
print("----------")
print(NAND(0, 0))
print(NAND(0, 1))
print(NAND(1, 0))
print(NAND(1, 1))
