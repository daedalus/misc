#!/bin/bash
set -x
DATA=$(cat $1)
USERID=$2
MAIL=$3
URL="http://factordb.com/report.php"
curl -X POST -F "report=$DATA" -F "format=0" -b "fbuser=$USERID" $URL | grep -e "Found" | grep -e factors > /tmp/result
cat $1 /tmp/result | mail $MAIL -s "Factoring results"
rm /tmp/result
