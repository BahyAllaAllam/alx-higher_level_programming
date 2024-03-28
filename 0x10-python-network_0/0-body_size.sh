#!/bin/bash
# Check if the user provided a URL
curl -s "$1" | wc -c

