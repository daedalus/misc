#!/bin/bash
# Author Dario Clavijo

INSTANCE=$1
PUB=1C8E0F39
TASKS=/var/lib/openvas/mgr/tasks.db
DST_DIR=/media/nfs/
docker $INSTANCE:$TASKS $HOME
gpg --always-trust --yes  --output $DST_DIR/tasks.db.gpg --encrypt --recipient $PUB $HOME/tasks.db
rm $HOME/tasks.db
