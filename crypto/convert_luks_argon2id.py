#!/bin/bash
# source https://mjg59.dreamwidth.org/66429.html
DEV=$1
lsblk
cryptsetup luksHeaderBackup /dev/$DEV --header-backup-file /tmp/luksheader
#cryptsetup luksHeaderRestore /dev/$DEV --header-backup-file luksheader
cryptsetup luksDump /dev/$DEV
cryptsetup convert /dev/$DEV --type luks2
cryptsetup luksDump /dev/$DEV
cryptsetup luksConvertKey /dev/$DEV --pbkdf argon2id
