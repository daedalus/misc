#!/bin/bash
# Author Darío Clavijo 2021
set -x
TOR_EXIT_NODES=/tmp/tor_exitnodes_ips.txt
wget https://check.torproject.org/torbulkexitlist -O $TOR_EXIT_NODES
for IP in $(cat $TOR_EXIT_NODES); do
   iptables -A INPUT -s $IP -j DROP
done
