#!/usr/bin/env python3
# Author Dario Clavijo 2023

import gnupg
import passboltapi
import json
import pwnedpasswords
import sys
from tqdm import tqdm
import urllib3
urllib3.disable_warnings()

passbolt = passboltapi.PassboltAPI(config_path="config.ini", new_keys=True)

def dec_resource_secret(id_):
  try:
    secret_gpg = passbolt.get(url="/secrets/resource/%s.json" % id_)['body']['data']
    gpg = gnupg.GPG()
    return json.loads(str(gpg.decrypt(secret_gpg)))['password']
  except:
    return None

sys.stderr.write("Gathering resources from passbolt...\n")
D = {}
for r in tqdm(passbolt.get(url="/resources.json?api-version=v2")['body']):
  #print(r)
  password = dec_resource_secret(r['id'])
  if password != None:
    t = (r['id'], r['name'],r['username'],r['uri'],r['description'])
    if password not in D:
      D[password] = [t]
    else:
      D[password].append(t)

sys.stderr.write("Checking passwords hashes against havibeenpwned...\n")
broken=[]
for password in tqdm(D):
  rating = pwnedpasswords.check(password, plain_text=True)
  if rating > 0:
    broken.append(password)

sys.stderr.write("Results:\n")

for password in broken:
  sys.stderr.write("-" * 60 + "\n")
  sys.stdout.write("-" * 60 + "\n")
  sys.stderr.write("broken password: %s\n" % password)
  sys.stdout.write("broken password: %s\n" % password)
  for t in D[password]:
    msg = "id:%s, name:%s, username:%s, uri: %s, description: %s\n" % t
    #sys.stderr.write("-" * 60 + "\n")
    #sys.stdout.write("-" * 60 + "\n")
    sys.stderr.write(msg)
    sys.stdout.write(msg)
  sys.stderr.flush()
  sys.stdout.flush()

sys.stdout.write("Total broken: %d\n" % len(broken))
sys.stdout.flush()
