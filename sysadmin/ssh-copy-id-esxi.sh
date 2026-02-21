#!/bin/bash
set -x

VMWHOST=$1

RSAPUB=$(cat .ssh/id_rsa.pub)
DSAPUB=$(cat .ssh/id_dsa.pub)
AUTHKEYS=/etc/ssh/keys-root/authorized_keys

ssh $VMWHOST -C "echo $RSAPUB >> $AUTHKEYS; echo $DSAPUB >> $AUTHKEYS"
