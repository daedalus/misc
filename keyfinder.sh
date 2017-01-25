#!/bin/bash
# Author Dario Clavijo 2017

set -x

cd $1
for f in *; do
        echo "filename:$f"
        aeskeyfind "$f" >> blk_aes.keys
        rsakeyfind "$f" >> blk_rsa.keys
done
