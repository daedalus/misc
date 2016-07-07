#!/bin/bash
set -x
for I in $(python -c "for i in range(0,35): print i*200") 
do
	curl -s "https://blockchain.info/tags?offset=$I" | grep -e tag | sed -e "s/[<>]/\n/g" | sort -u | grep -e "span class" -v >> /tmp/bci_tags
done

grep /tmp/bci_tags  -e script -v | grep -e input -v | grep -e "form action" -v | grep -e "a href" -v | sort -u > tmp/wordlists/bci_tags.txt
