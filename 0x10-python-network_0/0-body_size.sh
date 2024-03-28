#!/bin/bash
# Check if the user provided a URL
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-

