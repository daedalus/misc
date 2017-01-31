#!/bin/bash
set -x
ZRAM_SIZE_MB=512
modprobe zram && \
echo $((1024*1024*$ZRAM_SIZE_MB)) | tee /sys/block/zram0/disksize && \
mkswap /dev/zram0 && \
swapon -p 10 /dev/zram0 
