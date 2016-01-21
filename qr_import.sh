#!/bin/bash
#
# Author Dario Clavijo

wget $1 -O /tmp/qrcodeimg --quiet
#zbarimg /tmp/qrcodeimg
lines=$(zbarimg /tmp/qrcodeimg -q | grep -e QR | sed -e 's/QR-Code://g')
for line in $lines;
do 
	echo "$line"; 
	bitcoin-cli importprivkey $1 "" false
	echo $line >> tmp/scanned
done
