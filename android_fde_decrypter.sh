#!/bin/bash
# android FDE decryptor
# author Dario Clavijo 2018
# ref: https://www.forensicswiki.org/wiki/How_To_Decrypt_Android_Full_Disk_Encryption

set -x

PW=$1
DEV=$2
KEYFILE=/tmp/keyfile
EF=/tmp/encryption_footer

OFFSET=$(strings -t d $DEV | grep -e aes-cbc-essiv:sha256 | awk '{ print $1 }')
dd bs=1 skip=$(($OFFSET-36)) count=16384 if=$DEV of=$EF

curl https://raw.githubusercontent.com/daedalus/misc/master/android_fde_decryptkey.py > android_fde_decryptkey.py

python android_fde_decryptkey.py $EF $DEV $PW | xxd -r -ps > $KEYFILE

sudo cryptsetup \
    --cipher=aes-cbc-essiv:sha256 \
    --offset=0 \
    --type=plain \
    --key-file=$keyfile \
    --key-size=128  \
    open $DEV $DEV

rm $KEYFILE
rm $EF
