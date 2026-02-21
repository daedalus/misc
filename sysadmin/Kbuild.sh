#!/bin/bash

set -x
KV=4.19
KVL=4.19-rc7
VERSION="lowlatency-unsigned"

sudo apt-get install build-essential fakeroot kernel-package gcc gcc-8
sudo apt-get build-dep linux
sudo apt-get install libncurses5-dev libncursesw5-dev
sudo apt-get install linux-source-$KV

mkdir linux-build
cd linux-build
tar -xaf /usr/src/linux-source-$KVL.tar.xz
cd linux-source-$KVL

cat /boot/config-$(uname -r) | sed -e "s/# CONFIG_HZ_1000 is not set/CONFIG_HZ_1000=yes/g" | sed -e "s/CONFIG_HZ=250/CONFIG_HZ=1000/g" | sed -e "s/CONFIG_SYSTEM_TRUSTED_KEY/#CONFIG_SYSTEM_TRUSTED_KEY/g" > .config

#sudo make -j8 deb-pkg LOCALVERSION=-lowlatency KDEB_PKGVERSION=$(make kernelversion)-1
#cd ..
export CONCURRENCY_LEVEL=8
fakeroot make-kpkg -j $CONCURRENCY_LEVEL --arch amd64  --append-to-version -$VERSION --revision 1 --initrd kernel-image kernel_headers
if [ $? -eq 0 ]; then
    sudo dpkg -i linux-headers-$KV-$VERSION_$KVL-1_amd64.deb 
    sudo dpkg -i linux-image-$KV-$VERSION_$KVL-1_amd64.deb
fi
