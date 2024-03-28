#!/usr/bin/python3
from urllib.request import urlopen
import sys

url = sys.argv[1]

with urlopen(url) as req:
    headers = req.getheaders()
    for head in headers:
        if head[0].lower() == "x-request-id":
            print(head[1])
            break
    else:
        print("X-Request-Id header not found.")
