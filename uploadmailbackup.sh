#!/bin/bash
# Author Dario Clavijo 2017
# GPLv3

set -x

# setting up variables later needed
USER=dclavijo
RSA_PUB=1C8E0F39

MAILDIR=/home/$USER/.mail/
TMP_DISK=vdb1
DST_DISK=nfs_op
IMG=/media/$TMP_DISK/$USER/backup/mail.img
DST=/media/$DST_DISK/Respaldos/$USER/backup/mail_backup.gpg

# mounting the image
mount $IMG $MAILDIR

# mail getting stage
su $USER -c "getmail -n -g $MAILDIR/personal/.getmail/" 
su $USER -c "getmail -n -g $MAILDIR/work/.getmail/" 

sync

# deduping stage
duperemove -dhr -b 4k --hashfile=tmp/.mail_backup_hashfile_4k  $MAILDIR

# umounting image
umount $IMG
#lrzip -f -L 9 $IMG
#bzip2 $IMG

# compressing and encrypting stage
time lzop -k $IMG -c | lrzip -f -L 9 - > $IMG.lzo.lrz
time gpg -z 0 --always-trust --yes  --output $DST --encrypt --recipient $RSA_PUB $IMG.lzo.lrz

# cleaning up
rm $IMG.lzo.lrz
#rm /tmp/.hashfile4k
