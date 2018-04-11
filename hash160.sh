#!/bin/bash
# Author Dario Clavijo 2018
set -x

BIN=$HOME/tmp/hash160.bin
TXT=$HOME/tmp/hash160.txt
BLF=$HOME/tmp/bloom.blf

cp --reflink $BIN $BIN.bkp
cp --reflink $BLF $BLF.bkp

sort -u $1 | xxd -r -p >> $BIN
xxd -c 20 -ps $BIN > $TXT
sort -u $TXT | xxd -r -p > $BIN

code/BTC/brainflayer/hex2blf $TXT $BLF

rm $TXT
