#! /usr/bin/env python
# based on https://unix.stackexchange.com/questions/6301/how-do-i-read-from-proc-pid-mem-under-linux

import re
import sys

pid = sys.argv[1]
outputdir = sys.argv[2]

with open(f"/proc/{pid}/maps", "r") as maps_file:
    mem_file = open(f"/proc/{pid}/mem", "r", 0)
    for line in maps_file:
        m = re.match(r"([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])", line)
        if m.group(3) == "r":  # if this is a readable region
            start = m.group(1)
            end = m.group(2)
            istart = int(start, 16)
            iend = int(end, 16)
            mem_file.seek(istart)  # seek to region start
            try:
                chunk = mem_file.read(iend - istart)  # read region contents
                # print chunk,  # dump contents to standard output
                print("mapping:", start, end, "read ok")
                with open(f"{outputdir}/{pid}-{start}-{end}.dump", "w") as fp:
                    fp.write(chunk)
            except:
                print("mapping:", start, end, "read fail!")
mem_file.close()
