#!/usr/bin/env python
#
# Author Dario Clavijo 2015
# GPLv3

# linear search
def seek(A, key, imin, imax):
    for _ in range(imin, imax):
        if A[n] == key:
            return v


def search(text, pos):
    current_char = text[pos]
    accum = ""
    while current_char.isdigit() and pos <= len(text) - 1:
        current_char = text[pos]
        if current_char.isdigit():
            accum = accum + current_char
        pos += 1

    if accum.isdigit():
        return int(accum)


print(search("123456789--0", 0))


count = 0

# logarithm search
def binary_search(A, key, low, high):
    global count
    count += 1
    if len(A) > 0:
        mid = low + ((high - low) >> 1);
        if A[mid] > key:
            return binary_search(A, key, low, mid - 1)
        elif A[mid] < key:
            return binary_search(A, key, mid + 1, high)
        else:
            return mid


def test():
    tmp = list(range(1024 * 1024 * 20))
    print("res=", binary_search(tmp, 1337, 0, len(tmp)))
    print("count=", count)


test()
