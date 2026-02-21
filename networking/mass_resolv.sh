#!/bin/bash
# Author Darío Clavijo 2024
cat $1 | nslookup | grep -e "[Name|Address]"  | grep -e "#" -v | grep -e "Non" -v | grep -e "Server" -v | sed -e 's/\s//g;s/Name://g;s/Address://g;' | awk '{split($0,col1); getline; for (i=1; i<=NF; i++) print col1[i], $i}'
