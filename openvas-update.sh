#!/bin/sh
# Author Dario Clavijo 2016
set -x
LOG=/var/log/openvas/sync.log
DATE=$(date '+%d/%m/%Y %H:%M:%S')

echo "==========================================================================" >> $LOG
echo "|                 OpenVAS update Runing on $DATE          |" >> $LOG
echo "==========================================================================" >> $LOG

/usr/sbin/openvas-certdata-sync  >> $LOG
/usr/sbin/openvas-nvt-sync  >> $LOG
/usr/sbin/openvas-scapdata-sync >> $LOG

