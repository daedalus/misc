#!/bin/bash
# Author Dario Clavijo 2018

VM=$2
BKP=/home/dclavijo/.BKP/
IMG=/var/lib/libvirt/images
ETC=/etc/libvirt/qemu

function _undefine {
        virsh shutdown $VM
        virsh undefine $VM
        mv IMG/$VM* $BKP
        mv $ETC/$VM.xml $BKP
}

function _define {
        mv $BKP $IMG
        mv $BKP/$VM.xml $ETC
        virsh define $ETC/$BKP
        virsh start $VM
}

if [ "$1" = "-d" ]; then
        _define
fi

if [ "$1" = "-u" ]; then
        _undefine
fi
