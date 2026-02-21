# Flush file system buffers by executing
sync;

# free page cache
echo 1 > /proc/sys/vm/drop_caches;

# free dentries and inodes
echo 2 > /proc/sys/vm/drop_caches

# free page cache, dentries and inodes
echo 3 > /proc/sys/vm/drop_caches
