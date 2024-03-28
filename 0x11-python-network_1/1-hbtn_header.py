#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

with urlopen(url) as req:
    headers = req.getheaders()
    for head in headers:
        if header[0].lower() == "x-request-id":
            print(header[1])
            break
    else:
        print("X-Request-Id header not found.")

