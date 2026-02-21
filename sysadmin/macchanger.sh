#!/bin/bash
set -x
IF=wlan0
MAC=XX:XX:XX:XX:XX:XX
busybox ifconfig $IF hw ether $MAC
busybox ifconfig $IF down
busybox ifconfig $IF up
