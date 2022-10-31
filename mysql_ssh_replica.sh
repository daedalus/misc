#!/bin/bash
# Author Dario Clavijo 2022
set -x
HOST_DEST=$1
DATABASE=$2
ssh-copy-id root@$HOST_DEST
time mysqldump -u root $DATABASE -p | gzip -c | ssh root@$HOST_DEST -C "gzip -d | mysql -u root -p $DATABASE"
