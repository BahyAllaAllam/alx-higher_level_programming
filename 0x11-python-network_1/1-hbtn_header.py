#!/usr/bin/python3
"""
Python script that takes in a URL,
    sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
"""
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
