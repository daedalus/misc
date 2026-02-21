#!/bin/bash
set -x
modprobe -r rtl8188fu
git clone https://github.com/kelebek333/rtl8188fu
dkms add ./rtl8188fu
dkms build rtl8188fu/1.0
dkms install rtl8188fu/1.0
cp ./rtl8188fu/firmware/rtl8188fufw.bin /lib/firmware/rtlwifi/
mkdir -p /etc/modprobe.d/
touch /etc/modprobe.d/rtl8188fu.conf
echo "options rtl8188fu rtw_power_mgnt=0 rtw_enusbss=0" | sudo tee /etc/modprobe.d/rtl8188fu.conf
modprobe rtl8188fu
ifconfig wlx1cbfce8f64f8 up
iwlist scan
