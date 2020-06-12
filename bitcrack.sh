#!/bin/bash
# Author Dario Clavijo 2020
# GPLv3

set -x
DRIVEDIR='/content/drive/My Drive/BTC/'
OUT=$DRIVEDIR/out.txt
INPUT=$DRIVEDIR/INPUT.txt
RANGE="ffff:ffffffffffffffff"
COMPRESSION='compressed'
RANGE2=$(echo $RANGE | sed -e 's/:/_/g')
CONTINUE=$DRIVEDIR/bitcrack_continue.$COMPRESSION."$RANGE2".txt
MODEL=$(nvidia-smi | grep Tesla | awk '{ print $4 }')

if [ "$MODEL" == "T4" ]; then
  COMPUTE_CAP=75
fi
if [ "$MODEL" == "P100-PCIE..." ]; then
  COMPUTE_CAP=60
fi
if [ "$MODEL" == "P4" ]; then
  COMPUTE_CAP=61
fi
if [ "$MODEL" == "K80" ]; then
  COMPUTE_CAP=37
fi

mkdir '/content/drive/My Drive/BTC/'

EXTRA_OPTS=-b 36 -t 512 -p 2600

pwd
cd /content
#rm -rf BitCrack
git clone https://github.com/daedalus/BitCrack
cd BitCrack
#cat Makefile | sed -e "s/\/usr\/local\/cuda/\/usr\/local\/cuda-10.0\//g;s/COMPUTE_CAP=30/COMPUTE_CAP=$COMPUTE_CAP/g" > /tmp/Makefile
#mv /tmp/Makefile .
#grep Makefile -e COMPUTE_CAP
make BUILD_CUDA=1 COMPUTE_CAP=$COMPUTE_CAP -j 4
bin/cuBitCrack --compression "$COMPRESSION" --keyspace "$RANGE" --continue "$CONTINUE" --out "$OUT" --in "$INPUT" $EXTRA_OPTS
cd /content 
