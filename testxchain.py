import time  # Importing the time library to check the time of code execution
import sys  # Importing the System Library

import urllib2
import random
import hashlib
import os.path
import imghdr
import socket

timeout = 5
socket.setdefaulttimeout(timeout)

import hashlib


def sha256hex(s):
    return hashlib.sha256(s).hexdigest()


def download_page(url):
    version = (3, 0)
    cur_version = sys.version_info
    if cur_version >= version:  # If the Current Version of Python is 3.0 or above
        import urllib.request  # urllib library for Extracting web pages

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            }
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            return str(resp.read())
        except Exception as e:
            return None
    else:  # If the Current Version of Python is 2.x
        import urllib2

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            }
            req = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(req)
            return response.read()
        except:
            return None


def _get_next_item(s):
    # start_line = s.find('rg_di')
    # if start_line == -1:    #If no links are found then give an error!
    #    end_quote = 0
    #    link = "no_links"
    #    del start_line
    #    return link, end_quote
    # else:
    start_line = s.find("<td id='phrasecol'>")
    start_content = s.find("<pre>", start_line + 1)
    end_content = s.find("</pre>", start_content + 1)
    content_raw = str(s[start_content + 6 : end_content - 1])

    # print start_line,start_content,end_content
    # del start_line
    # del start_content

    if start_line == -1:
        content_raw = "no_links"

    return content_raw, end_content


import fileinput

for line in fileinput.input():
    addr = line.rstrip()
    url = "https://xchain.io/api/balances/%s" % addr
    raw_html = download_page(url)
    if raw_html != '{"error":"Address not found"}':
        print addr, raw_html
