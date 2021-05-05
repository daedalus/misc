#!/usr/bin/env python
# Author Dario Clavijo 2018
import os
import time
import sys


def beep(f):
    os.system("play -q -n synth 0.1 sin %d" % f)


def gettemp():
    fp = open("/sys/class/thermal/thermal_zone0/temp", "r")
    temp = float(fp.read()) / 1000
    fp.close()
    return temp


def getfan():
    fp = open("/sys/devices/platform/asus-nb-wmi/hwmon/hwmon2/fan1_input")
    rpm = int(fp.read())
    fp.close()
    return rpm


def setfan():
    os.system("echo 255 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon2/pwm1")
    # os.system('paplay /usr/share/sounds/gnome/default/alerts/glass.ogg')
    time.sleep(2)
    os.system(
        "echo 2 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon2/pwm1_enable"
    )


while True:
    temp = gettemp()
    sys.stdout.write("\r" + str(temp))
    sys.stdout.flush()
    rpm = getfan()
    if temp > 80:
        setfan()
    # if temp > 90:
    #    beep()
    os.system(
        "echo 'temp: %d C,fan: %d' | osd_cat --lines=1 --font='lucidasanstypewriter-bold-8'"
        % (temp, rpm)
    )
    time.sleep(2)
