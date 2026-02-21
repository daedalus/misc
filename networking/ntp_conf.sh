#!/bin/bash
#Autor Dario Clavijo 2018

set -x

CONF=/etc/ntp.conf
apt-get install ntp -y

mv "$CONF" "$CONF"_orig

cat > $CONF <<- EOM
driftfile /var/lib/ntp/ntp.drift
statistics loopstats peerstats clockstats
filegen loopstats file loopstats type day enable
filegen peerstats file peerstats type day enable
filegen clockstats file clockstats type day enable
pool SERVER1 iburst
pool SERVER2 iburst
restrict -4 default kod notrap nomodify nopeer noquery limited
restrict -6 default kod notrap nomodify nopeer noquery limited
restrict 127.0.0.1
restrict ::1
restrict source notrap nomodify noquery
EOM

/etc/init.d/ntp restart
date
