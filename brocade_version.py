#!/usr/bin/env python
#
# script que obtiene la version de fabric os de los fcsw brocade
#
# v1.0 initial version

import fileinput
import sys
import re
import paramiko

# execute a remote command by ssh
def exec_ssh(host, user, passwd, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdout.readlines()


for line in fileinput.input():
    line = line.rstrip()
    try:
        ret = line, exec_ssh(line, "USER", "PASS", "version")
        for version in ret[1]:
            if re.search("Fabric", version):
                print(ret[0], version.rstrip())
    except:
        print(line, "failed")
