#!/bin/bash
set -x
sudo apt-get update
sudo apt-get install libboost-all-dev ccache libcrypto++-dev libdb++-dev libboost-dev libboost-all-dev
git clone https://github.com/bitcoin/bitcoin
cd bitcoin/
./autogen.sh
./configure --prefix=`pwd`/depends/x86_64-pc-linux-gnu --with-incompatible-bdb --disable-hardening  --disable-tests --disable-bench
make -j 8
