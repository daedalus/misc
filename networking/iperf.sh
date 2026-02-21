#!/bin/bash
# iperf tests automation
# Dario Clavijo 2017

set -x
IP_SERVER=$1
P0RT=$2
IPERF_OPTS="-c $IP_SERVER -d  -t 14400 -i 10 -p $PORT"

ssh $IP_SERVER -C "iperf -s -p $PORT"
iperf $IPERF_OPTS > test_iperf_$IP_SERVER.txt 2>/dev/null
ping $IP_SERVIDOR > test_ping_$IP_SERVER.txt 2>/dev/null

tar czf iperf_Tests_$DATE.tar.gz test_iperf_$IP_SERVER.txt test_ping_$IP_SERVER.txt
