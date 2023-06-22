#!/usr/bin/python
# Author Darío Clavijo 2023

import sys
import re
import paramiko
import time

host =  sys.argv[1]
user = sys.argv[2]
passwd = sys.argv[3]

class Cisco():
    
  def __init__(self, host, user, passwd, wait=0.5, recv_len=65535):
    self.host = host
    self.user = user
    self.passwd = passwd
    self.wait = wait
    self.recv_len = recv_len
    self.ssh = paramiko.SSHClient()
    self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    self.ssh.connect(hostname=host, username=user, password=passwd)
    self.shell = self.ssh.invoke_shell()

  def enable(self, ena_password):
    self.shell.send("enable\n")
    time.sleep(self.wait)
    self.shell.send("%s\n" % ena_password)
    time.sleep(self.wait)

  def command(self, cmd):
    self.shell.send("%s\n" % cmd)
    time.sleep(self.wait)
    return self.shell.recv(self.recv_len)


C = Cisco(host, user, passwd)
C.enable("cisco")
print(C.command("conf t").decode("utf8"))
