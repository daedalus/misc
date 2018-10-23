#!/bin/bash
set -x
mount -o rw,remount /system
curl https://adaway.org/hosts.txt > /etc/hosts
