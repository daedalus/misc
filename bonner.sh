#!/bin/bash
# Author Dario Clavijo 2016
# GPLv3

set -x

DIR=/tmp/
SIZE=100M
KFILES=2
TESTS=2
USER=root

date=$(date +"%H%M%S-%d%m%Y")

HTML_OUTPUT_FILE=/var/www/html/bonnie/bonnie_"$HOSTNAME"_$date.html

OPTS="-f -b -r 0 -q"

/usr/sbin/bonnie -d $DIR -s $SIZE -n $KFILES -m $HOSTNAME -u $USER -x $TESTS $OPTS  > /tmp/bonnie.csv

cat /tmp/bonnie.csv | bon_csv2html > $HTML_OUTPUT_FILE
