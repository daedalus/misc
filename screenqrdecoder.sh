#!/bin/bash
# Author Dario Clavijo 2016

TMP=$(mktemp --suffix .qrdecode.jpg)
gnome-screenshot -a --file=$TMP
DECODED=$(zbarimg $TMP)
echo $DECODED >> $HOME/qrdecoded
rm $TMP

