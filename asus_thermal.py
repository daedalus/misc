#!/usr/bin/env python
# Author Dario Clavijo 2018
import os
import time
while True:
    fp=open('/sys/class/thermal/thermal_zone0/temp','r')
    temp=float(fp.read())/1000
    print temp
    fp.close()
    if temp > 85:
        os.system('echo 255 | tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon2/pwm1')
        os.system('paplay /usr/share/sounds/gnome/default/alerts/glass.ogg')
        time.sleep(2)
        os.system('echo 2 | tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon2/pwm1_enable')
    else:
        time.sleep(2)
