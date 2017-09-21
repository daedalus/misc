#!/bin/bash
# ALEXCTF{SN1FF_TH3_FL4G_0V3R_USB} SOL
# Author Dario Clavijo 2017
# GPLv3

set -x

FILENAME=$1
START=$(grep --byte-offset --only-matching --text "PNG" $FILENAME | sed -e "s/:/ /g" | awk '{ print $1 }')
END=$(tshark -nr $FILENAME frame contains PNG | awk '{ print $7 }')
python ./file_cut_simple.py $FILENAME $(echo "$START - 1"| bc) $END > flag.png
