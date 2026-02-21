#!/bin/bash
# Author Dario Clavijo 2018
set -x
export mesa_glthread=true
export WINEDEBUG=-all,+fps
export DISPLAY=:3
LOG=/tmp/GAME.log
LOG2=/tmp/qemu.log

GAMEDIR='Games/Game'
GAMEEXE='Game.exe'
GAMEOPTS='-dx9'

cd $GAMEDIR

function display_stats {
    TEMP=$(acpi -t | awk '{ print $4 }')
    FPS=$(tail -n 1 $LOG)
    echo "$FPS $TEMP C" | osd_cat --lines=1 --font='lucidasanstypewriter-bold-8'
}

function gamerun {
	if [ $1 == 'normal' ]; then
		startx /usr/bin/wine64-development $GAMEEXE $GAMEOPTS -- $DISPLAY 2>&1 | sed -u -n -e '/trace/ s/.*approx //p' >> $LOG &
	fi
	if [ $1 == 'virt']; then
		startx /usr/bin/qemu-x86_64 /usr/bin/wine64-development $GAMEEXE $GAMEOPTS -- $DISPLAY 2>&1 | sed -u -n -e '/trace/ s/.*approx //p' >> $LOG &
	fi
	if [ $1 == 'virt-debug' ]; then
		startx /usr/bin/qemu-x86_64 -strace -d pcall,exec,guest_errors,mmu -D $LOG2 /usr/bin/wine64-development $GAMEEXE $GAMEOPTS -- $DISPLAY 2>&1 | sed -u -n -e '/trace/ s/.*approx //p' >> $LOG &
	fi
}

if [[ $1 == '' ]]; then
	gamerun 'normal'
else
	gamerun $1
fi

while sleep 5; do
    display_stats
done

#rm $LOG 
