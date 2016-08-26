#!/bin/sh
# Author Dario Clavijo 2016

set -x

LOG=/var/log/openvas/sync.log

/usr/sbin/openvas-certdata-sync  >> $LOG
/usr/sbin/openvas-nvt-sync  >> $LOG
/usr/sbin/openvas-scapdata-sync >> $LOG
