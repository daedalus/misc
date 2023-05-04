#!/usr/bin/env python3
# Author Dario Clavijo 2023

import gnupg
import passboltapi
import json
import pwnedpasswords
import sys

passbolt = passboltapi.PassboltAPI(config_path="config.ini", new_keys=True)

def dec_resource_secret(id_):
  try:
    secret_gpg = passbolt.get(url="/secrets/resource/%s.json" % id_)['body']['data']
    gpg = gnupg.GPG()
    return json.loads(str(gpg.decrypt(secret_gpg)))['password']
  except:
    return None

for r in passbolt.get(url="/resources.json?api-version=v2")['body']:
  password = dec_resource_secret(r['id'])
  if password != None:
    rating = pwnedpasswords.check(password)
    if rating > 0:
      msg = "<" + r['id'] + "><" + r['name'] + "><" + password + ">"
      sys.stderr.write("-*60")
      sys.stderr.write(msg + "\n")
      sys.stdout.write(msg + "\n")
      sys.stderr.flush()
      sys.stdout.flush()

