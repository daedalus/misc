#!/bin/bash
filename="$1"
POOL="$2"
USER="$3"

while read -r line
do
    reply=$(torify  $HOME/code/BTC/cgminer/cgminer-api "addpool|stratum+tcp://$POOL,$USER.1,xxxx" $line 4028)
    echo $line $reply >> scan_log
done < "$filename"
