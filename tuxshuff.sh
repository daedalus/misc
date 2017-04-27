#!/bin/bash
# Tux AES ECB MODE LEAK INFO FLAW
# Author Dario Clavijo 2016

set -x

convert tux.png tux.ppm
head -n 4 tux.ppm > tux.header.ppm
tail -n +5 tux.ppm > tux.data.ppm

cat tux.data.ppm | python shuffledata.py > tux.data.shuff.ppm

cat tux.header.ppm tux.data.shuff.ppm > tux.shuff.ppm  

