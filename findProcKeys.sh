#!/bin/bash
# Author Dario Clavijo 2018

function _ReadProcMemByPid {
    python readprocmem.py $1 /tmp/
    for f in /tmp/*.dump; do
    
        RSAKEY=$f.rsa.key
        AESKEY=$f.aes.key

        rsakeyfind $f > $RSAKEY
        aeskeyfind -q $f > $AESKEY

        if [ ! -s $RSAKEY ] ; then rm $RSAKEY; fi
        if [ ! -s $AESKEY ] ; then rm $AESKEY; fi
    done
    rm /tmp/*.dump
}

function _ProcsByName {
    for pid in $(ps aux | grep -e $1 | awk '{ print $2 }'); do
        _ReadProcMemByPid $pid
    done
}

function _AllProcs {
    for pid in $(ps aux | tail -n +2 | awk '{ print $2 }'); do
        _ReadProcMemByPid $pid
    done
}

if [ ! -f /usr/bin/rsakeyfind ]; then
        echo "rsakeyfind not found!"
        exit 0
fi
if [ ! -f /usr/bin/aeskeyfind ]; then
        echo "aeskeyfind not found!"
        exit 0
fi

if [ "$1" = "-p" ]; then
    _ReadProcMemByPid $2
elif [ "$1" = "-n" ]; then
    _ProcsByName $2
elif [ "$1" = "-a" ]; then 
    _AllProcs  
else
    #set +x
    echo """usage: $0 [opt] [arg]
    -p PID            Single process
    -n ProcessName    All process by name
    -a                Allprocess"""
fi
