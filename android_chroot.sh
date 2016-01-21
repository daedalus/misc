export SDCARD=/sdcard
export ROOT=$SDCARD/debian
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH
export HOME=/root
mount -o remount,exec,dev,suid $SDCARD
for f in dev dev/pts proc sys ; do mount -o bind /$f $ROOT/$f ; done
chroot $ROOT /bin/bash -l
debootstrap/debootstrap --second-stage
