#!/bin/bash

# source: https://gist.github.com/mgeeky/5e36d6482e73ab85c161c35bfd50c465

echo -e "\n\nSimple SSL/TLS self-signed CA Certificate generator\n\n" 

if [ -z $1 ]; then
	echo "Usage: $0 [file_name] [hostname]"
	echo -e "\nGoing with default name: './rogue_server'\n\n"
fi

YOUR_HOST=$2
FILENAME=${1:-rogue_server}

echo "[+] Generating public and private keys pair (.key)..."
openssl genrsa -out $FILENAME.key 1024

echo "[+] Generating a self-signed x509 CA's certificate (.crt)..."
openssl req -new -key $FILENAME.key -x509 -sha256 -days 3600 -out $FILENAME.crt -subj "/"

echo "[+] Generating the PEM file out of the key and certificate files..."
cat $FILENAME.key $FILENAME.crt > $FILENAME.pem

echo -e "\n[>] Certificate's dump:"
openssl x509 -in $FILENAME.pem -text -noout

echo -e "\n[>] Generated files:"
echo -e "\tPKI keys (public/private):\t$FILENAME.key"
echo -e "\tCA Certficate:\t\t$FILENAME.crt"
echo -e "\tResulting PEM:\t\t$FILENAME.pem"

echo -e "\n\n[+] Now you can start a TLS-enabled server with:\n"
sudo socat -vv openssl-listen:443,reuseaddr,fork,cert=$FILENAME.pem,cafile=$FILENAME.crt,verify=0 openssl-connect:$YOUR_HOST,verify=0
echo "Happy MITM-ing!"
