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

    date=$(date +"%H%M%S-%d%m%Y")

    SIZE2=$(echo $SIZE | sed -e 's/\:/_/g')

    HTML_OUTPUT_FILE=bonnie_"$SIZE2"_"$HOSTNAME"_"$DEVICE"_$date.html

    #OPTS="-f -b -r 0 -q -D -c 200"
    OPTS="-f -b -r 0 -q -c 200"

    /usr/sbin/bonnie -d $DIR -s $SIZE -n $KFILES -m $HOSTNAME -u $USER -x $TESTS $OPTS  > /tmp/bonnie.csv

    cat /tmp/bonnie.csv | bon_csv2html > $HTML_OUTPUT_FILE
}

bonne $1
