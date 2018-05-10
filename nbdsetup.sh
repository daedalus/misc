#!/bin/bash
set -x

USER=dclavijo
IMG=test
DISK=nbd0
SIZE=16G

modprobe nbd max_part=8
qemu-img create -f qcow2 $IMG.qcow2 $SIZE
qemu-nbd --connect=/dev/$DISK $IMG.qcow2 
cryptsetup luksFormat /dev/$DISK 
cryptsetup luksOpen /dev/$DISK $DISK
mkfs.btrfs /dev/mapper/$DISK
mkdir /media/dclavijo/$DISK
mount /dev/mapper/$DISK /media/$USER/$DISK
chown $USER:$USER /media/$USER/$DISK
