#!/bin/bash
# Author Darío Clavijo 2023
set -x

/sbin/adduser bitwarden
/sbin/groupadd docker
/sbin/usermod -aG docker bitwarden
mkdir /opt/bitwarden
chmod -R 700 /opt/bitwarden
chown -R bitwarden:bitwarden /opt/bitwarden
cd /opt/bitwarden

apt-get update && apt-get install curl docker.io docker-compose -y
curl -Lso bitwarden.sh "https://func.bitwarden.com/api/dl/?app=self-host&platform=linux" && chmod 700 bitwarden.sh

./bitwarden.sh install
./bitwarden.sh start
