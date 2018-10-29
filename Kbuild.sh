#!/bin/bash

set -x
KV=4.19
apt-get install build-essential fakeroot
apt-get build-dep linux
apt-get install libncurses5-dev libncursesw5-dev
apt-get install linux-source-$KV
tar -xaf /usr/src/linux-source-$KVtar.xz
cd linux-source-$KV
cp $CFG .config
make menuconfig

#FIXME
#In the gui:
#enable preempt
#enable timers 1000Hz

make -j4 deb-pkg LOCALVERSION=-lowlatency KDEB_PKGVERSION=$(make kernelversion)-1
cd ..
dpkg -i linux-headers-$KV-lowlatency_$KV-1_amd64.deb 
dpkg -i linux-image-$KV-lowlatency_$KV-1_amd64.deb
