#!/bin/bash
# Tux AES ECB MODE LEAK INFO FLAW
# Author Dario Clavijo 2016

set -x

convert tux.png tux.ppm
head -n 4 tux.ppm > tux.header.ppm
tail -n +5 tux.ppm > tux.data.ppm
openssl enc -aes-128-cbc -nosalt -pass pass:"dario" -in tux.data.ppm -out tux.data.cbc.bin
openssl enc -aes-128-ecb -nosalt -pass pass:"dario" -in tux.data.ppm -out tux.data.ecb.bin
cat tux.header.ppm tux.data.cbc.bin > tux.cbc.ppm  
cat tux.header.ppm tux.data.ecb.bin > tux.ecb.ppm  

rm tux.ppm tux.header.ppm tux.data.ecb.bin
