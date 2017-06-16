import time       #Importing the time library to check the time of code execution
import sys    #Importing the System Library

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
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            #print (len(respData) // 1024),"KB"


            return respData
        except Exception as e:
            return None
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            #print (len(page) // 1024),"KB"

            return page
        except:
            return None


def _get_next_item(s):
    #start_line = s.find('rg_di')
    #if start_line == -1:    #If no links are found then give an error!
    #    end_quote = 0
    #    link = "no_links"
    #    del start_line
    #    return link, end_quote
    #else:
	ltag=5
	start_line = s.find("<td id='phrasecol'>")
        start_content = s.find("<pre>",start_line)
        end_content = s.find("</pre>",start_content)
        content_raw = str(s[start_content+ltag:end_content-1])
     
	#print start_line,start_content,end_content
	#del start_line
        #del start_content
        
	if start_line == -1:	
		content_raw = "no_links"

	return content_raw, end_content


def _get_all_items(page):
    items = []
    #print len(page)
    while True:
        item, end_content = _get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            #time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
        if len(item) > 10000:
                break
    return items


for i in xrange(0,15):
	url = 'https://bitsig.io/?page=%d' % i
	raw_html = (download_page(url))
	items = _get_all_items(raw_html)

	for item in items:
		item = item.replace('\n\r','\r')
		#print item.encode('hex')
		print sha256hex(item)
