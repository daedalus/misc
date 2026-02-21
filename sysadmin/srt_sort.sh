#!/bin/bash

# make a compilation of every srt line into a single sorted file .gz

find $1/ -name "*.srt" -print0 | while IFS= read -r -d '' file; do
     echo "file = $file";
     cat $line >> /tmp/srt.txt
done
cat /tmp/srt.txt | sort -u | gzip -c > srt.gz
