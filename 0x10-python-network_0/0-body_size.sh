#!/bin/bash

# Check if the user provided a URL
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a GET request to the URL and save the response to a file
response_size=$(curl -s -w "%{size_download}" -o /dev/null "$1")
echo "$response_size"

