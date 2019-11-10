#!/bin/bash
set -x
USERID=$2
URL="http://factordb.com/report.php"
DATA=$(cat $1)
curl -X POST -F "report=$DATA" -F "format=0" -b "fbuser=$USERID" $URL | grep -e "Found" | grep -e factors > /tmp/result
cat $1 | mail daedalus2027@gmail.com -s "Factoring results"
