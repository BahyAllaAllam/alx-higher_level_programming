#!/bin/bash
# Check if the user provided a URL
curl -s -w "%{size_download}" -o /dev/null "$1"

