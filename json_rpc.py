#!/usr/bin/env python
#Author Dario Clavijo 2020
#GPLv3

import requests
import json

class rpc():
  def __init__(self,url,rpcuser,rpcpassword):
    self.rpcuser=rpcuser
    self.rpcpassword=rpcpassword
    self.url = url % (rpcuser,rpcpassword)

  def _rpccall(self,payload):
    #print self.url,payload
    return requests.post(self.url, json=payload).json()

  def rpccall(self,method,params):
    payload = {
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 0,
    }
    return self._rpccall(payload)
