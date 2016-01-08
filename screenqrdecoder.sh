#!/bin/bash
# Author Dario Clavijo 2016

TMP=$(mktemp).jpg
gnome-screenshot -a --file=$TMP
DECODED=$(zbarimg $TMP)
echo $DECODED
echo $DECODED >> $HOME/qrdecoded
