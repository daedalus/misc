#!/bin/bash

set -x

POOL=$1
IMG=$2
SIZE=$3
PAGES=$4
USER=$5
LDEV=$6 # example rbd0
FS="mkfs.ext4 -j"
MONITOR="172.16.1.1 172.16.2.2"

ceph osd pool create $POOL $PAGES
rbd pool init $POOL
rbd create --size $SIZE $POOL/$IMG

ceph auth get-or-create client.$USER mon "allow r" osd "allow class-read object_prefix rbd_children, allow rwx pool=$POOL"
KEY=$(ceph auth get-or-create client.$USER)

rbd feature disable $POOL/$IMG fast-diff
rbd feature disable $POOL/$IMG deep-flatten
rbd feature disable $POOL/$IMG object-map

echo "#!/bin/bash" > deploy_$USER.sh
echo "echo deploying ceph..." >> deploy_$USER.sh
echo "sudo apt-get install ceph-common" >> deploy_$USER.sh
echo "sudo modprobe rbd" >> deploy_$USER.sh
echo "sudo echo '$MONITOR name=$USER,secret=$KEY $POOL $IMG' | sudo tee /sys/bus/rbd/add" >> deploy_$USER.sh
echo "sudo $FS /dev/$LDEV" >> deploy_$USER.sh
echo "sudo mkdir /media/$LDEV" >> deploy_$USER.sh
echo "sudo mount /dev/$LDEV /media/$LDEV" >> deploy_$USER.sh
