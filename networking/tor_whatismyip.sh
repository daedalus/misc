#!/bin/bash
# Author Dario Clavijo 2020
# GPLv3
torify curl -s whatismyip.com | grep -e "Your IP" | grep -e "[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}" -o
