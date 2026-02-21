#!/bin/bash
set -x

OLD=$1
NEW=$2

vgrename $OLD $NEW

sed -i 's/$OLD/$NEW/g' /boot/grub/grub.cfg
sed -i 's/$OLD/$NEW/g' /etc/fstab
sed -i 's/$OLD/$NEW/g' /etc/initramfs-tools/conf.d/resume

vgscan 
vgchange -ay
update-initramfs -u -k all
update-grub
