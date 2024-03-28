#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    request_id = response.getheader('X-Request-Id')
    if request_id:
        print(request_id)
