#!/bin/bash
# Check if the user provided a URL
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2

