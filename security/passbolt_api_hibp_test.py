#!/usr/bin/env python3
# Author Dario Clavijo 2023

import passboltapi
import json
import pwnedpasswords
import sys
from tqdm import tqdm
import urllib3

urllib3.disable_warnings()
passbolt = passboltapi.PassboltAPI(config_path="config.ini", new_keys=True)


def load_dict(passbolt):
    """
    loads into a dictionary resources grouped by their passwords
    output: dictionary
    """
    sys.stderr.write("Gathering resources from passbolt...\n")
    D = {}
    for r in tqdm(passbolt.get(url="/resources.json?api-version=v2")["body"]):
        password = passbolt.get_password(r["id"])
        if password != None:
            t = (r["id"], r["name"], r["username"], r["uri"], r["description"])
            if password not in D:
                D[password] = [t]
            else:
                D[password].append(t)
    return D


def proc_dict(passbolt, D):
    """
    Checks every password in the dictionary if its broken.
    input: dictionary
    output: broken_plain_password_list
    """
    sys.stderr.write("Checking passwords hashes against HIBP...\n")
    broken = []
    for password in tqdm(D):
        rating = pwnedpasswords.check(password, plain_text=True)
        if rating > 0:
            broken.append(password)
    return broken


def display_broken(broken):
    """
    Display info in the dictionary using elements of broken list as key.
    input: broken_plain_password_list
    """
    sys.stderr.write("Results:\n")
    for password in broken:
        sys.stderr.write("-" * 60 + "\n")
        sys.stdout.write("-" * 60 + "\n")
        sys.stderr.write("broken password: %s\n" % password)
        sys.stdout.write("broken password: %s\n" % password)
        for t in D[password]:
            msg = "id:%s, name:%s, username:%s, uri: %s, description: %s\n" % t
            sys.stderr.write(msg)
            sys.stdout.write(msg)
        sys.stderr.flush()
        sys.stdout.flush()
    sys.stderr.write("Total broken: %d\n" % len(broken))
    sys.stderr.flush()


if __name__ == "__main__":
    D = load_dict(passbolt)
    broken = proc_dict(passbolt, D)
    display_broken(broken)
