#!/usr/bin/env python
# Copyright Dario Clavijo 2017
# GPLv3

import sys
import libkeepass


def human_readable_dump():
    with libkeepass.open(filename=sys.argv[1], password=sys.argv[2]) as kdb:
        root = kdb.tree.getroot()
        for group in root.Root.iter("Group"):
            try:
                print "GROUP:", group.Name
                for Entry in group.iter("Entry"):
                    print "\t" + "=" * 80
                    for string in Entry.iter("String"):
                        print "\t\t" + "-" * 80
                        print "\t\t" + string["Key"] + ":" + string["Value"]

            except:
                pass
        print "=" * 80


def xml_dump():
    with libkeepass.open(filename=sys.argv[1], password=sys.argv[2]) as kdb:
        print kdb.pretty_print()


human_readable_dump()
