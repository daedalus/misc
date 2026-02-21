#!/usr/bin/env python
# author Dario Clavijo 2016
# GPLv3


def make_crc_table(const):
    testcrc = []
    for i in range(0, 256):
        temp = i
        for _ in range(0, 8):
            if temp & 1:
                temp >>= 1
                temp ^= const
            else:
                temp >>= 1
        testcrc.append(temp)
    return testcrc


def displaytable(table):
    string_hex_line = "".join(hex(i) for i in numbers)
    print(string_hex_line)


numbers = make_crc_table(0xEDB88320)
displaytable(numbers)

numbers = make_crc_table(0x04C11DB7)
displaytable(numbers)
