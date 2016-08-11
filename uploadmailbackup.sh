#!/bin/bash
# author Darío Clavijo 2016
# GPLv3

set -x

USER=dclavijo
RSA_PUB=1C8E0F39

MAILDIR=/home/$USER/mail/
TMP_DISK=vdb1
DST_DISK=my_nfs_server
IMG=/media/$TMP_DISK/$USER/backup/mail.img
DST=/media/$DST_DISK/$USER/backup/mail_backup.gpg

su $USER -c "getmail -n"
sync
umount $IMG
lrzip -f -L 9 $IMG
gpg -z 0 --always-trust --yes  --output $DST --encrypt --recipient $RSA_PUB $IMG.lrz
mount $IMG $MAILDIR
