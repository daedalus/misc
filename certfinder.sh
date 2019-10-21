#!/bin/bash
DEST=/tmp/CERTS
mkdir $DEST
find / -name *.pem | xargs -I{} cp -u {} $DEST
find / -name *.der | xargs -I{} cp -u {} $DEST
find / -name *.cert | xargs -I{} cp -u {} $DEST
find / -name *.crt | xargs -I{} cp -u {} $DEST
find / -name *.RSA | xargs -I{} cp -u {} $DEST
tar czf CERTS.tar.gz $DEST
rm -rf $DEST
