#!/bin/bash
set -x
DEST=/tmp/CERTS
mkdir $DEST
find / -name *.pem | xargs -I{} cp --backup  {} $DEST
find / -name *.der | xargs -I{} cp --backup  {} $DEST
find / -name *.cert | xargs -I{} cp --backup {} $DEST
find / -name *.crt | xargs -I{} cp --backup {} $DEST
find / -name *.RSA | xargs -I{} cp --backup {} $DEST
tar czf CERTS.tar.gz $DEST
rm -rf $DEST
