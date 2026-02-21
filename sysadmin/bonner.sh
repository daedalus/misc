#!/bin/bash
# Author Dario Clavijo 2016
# GPLv3

set -x

function bonne {
	DEVICE=$1
	SIZE="1G:4k"
	KFILES=2
	TESTS=10
	USER=root
	DIR=/media/$DEVICE
	DEVNAME=$(multipath -l | grep -e $DEVICE | awk '{ print $3 }' | sed -e "s/,/_/g")

	date=$(date +"%H%M%S-%d%m%Y")

	HTML_OUTPUT_FILE=/var/www/html/bonnie/bonnie_"$SIZE"_"$HOSTNAME"_"$DEVICE"_"$DEVNAME"_$date.html

	OPTS="-f -b -r 0 -q"

	/usr/sbin/bonnie -d $DIR -s $SIZE -n $KFILES -m $HOSTNAME -u $USER -x $TESTS $OPTS  > /tmp/bonnie.csv

	cat /tmp/bonnie.csv | bon_csv2html > $HTML_OUTPUT_FILE
}

# example only, edit below lines with real wwns
bonne 360060000000000000000000000000000-part1 # lun 0
bonne 360060000000000000000000000000001-part1 # lun 1
