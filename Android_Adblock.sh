#!/bin/bash
mount -o remount,rw /system
curl http://adaway.org/hosts.txt >> /etc/hosts
