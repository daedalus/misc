#!/bin/bash
# Author Darío Clavijo 2023
APK=$1
cat $APK | pm install -i "com.android.vending" -S $(stat $APK -c "%s")
rm $APK
