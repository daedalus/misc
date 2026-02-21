#!/bin/bash
set -x

/bin/btrfs-find-root -a /dev/sdb1 | sed -e 's/[\(\)]/ /g' | awk '{ print $3 }' >> /tmp/extents.txt

while IFS='' read -r line || [[ -n "$line" ]]; do
    btrfs restore -t $line /dev/sdb1 /media/sdc1/
done < /tmp/extents.txt
