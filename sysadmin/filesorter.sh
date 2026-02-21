#!/bin/bash
# Author Darío Clavijo 2016

set -x

md5sum $1/* > /tmp/md5
mkdir sorted
cat /tmp/md5 | awk 'BEGIN { FS="  " } /1/ { print "mv -" $2 "- "  "sorted/"$1".dat" }' | sed -e 's/-/"/g'
