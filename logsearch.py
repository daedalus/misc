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
def seeklog(A, key, imin, imax):
    global count
    count += 1

    if len(A) > 0:
        imid = (imax + imin) / 2
        if A[imid] > key:
            return seeklog(A, key, imin, imid - 1)
        elif A[imid] < key:
            return seeklog(A, key, imid + 1, imax)
        else:
            return imid


def test():
    tmp = list(range(1024 * 1024 * 20))
    print("res=", seeklog(tmp, 1337, 0, len(tmp)))
    print("count=", count)


test()
