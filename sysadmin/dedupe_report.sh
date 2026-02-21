#!/bin/bash
#
# Author Dario Clavijo

DRIVE=$1

#for SIZE in 1024 512 256 128 64 32 16 8 4
for SIZE in 512 256 128 64 32 16 8 4
mkdir /tmp/dedupe_reports
do
	LOG=/tmp/dedupe_reports/$SIZE.log
	duperemove -r -d -b "$SIZE"k $DRIVE >> $LOG
done
