#!/bin/bash
# Author Dario Clavijo 2016
# GPLv3

set -x

DIR=/tmp/
SIZE=2G
KFILES=2
TESTS=2
USER=root

SOPTS="-f -b -r 0 -q"

date=$(date +"%H%M%S-%d%m%Y")

/usr/sbin/bonnie -d $DIR -s $SIZE -n $KFILES -m $HOSTNAME -u $USER -x $TESTS $SOPTS  > /tmp/bonnie.csv

cat /tmp/bonnie.csv | bon_csv2html > /var/www/html/bonnie/bonnie_$HOSTNAME_$date.html
