#!/bin/bash
# Author Dario Clavijo 2018
set -x
export WINEDEBUG=fps 
export DISPLAY=:3
LOG=/tmp/.$1.fps.log
GAME=$1 # YOUR GAME's EXE

function display_stats {
    TEMP=$(acpi -t | awk '{ print $4 }')
    FPS=$(tail -n 1 $LOG)
    echo "$FPS $TEMP C" | osd_cat --lines=1 --font='lucidasanstypewriter-bold-8'
}

function wine_run {
    startx /usr/bin/wine64-development $1 -- $DISPLAY 2>&1 | sed -u -n -e '/trace/ s/.*approx //p' >> $LOG &
}

wine_run $1

while sleep 5; do
    display_stats
done

rm LOG
