#!/bin/bash
set -x
URL="http://factordb.com/report.php"
curl -X POST -F "report=$(cat $1)" -F "format=11" $URL | grep -e "Found" | grep -e factors
