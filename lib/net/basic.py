# !/usr/bin/env python

import httplib2

def http(link):
    h = httplib2.HTTP(".cache")
    print ("[-] Requesting ", link)
    resp, cont = h.request(link)
    return cont
