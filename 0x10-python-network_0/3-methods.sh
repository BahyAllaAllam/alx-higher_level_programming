#!/bin/bash
# Bash script that sends a DELETE request.
curl -sX OPTIONS -i "$1" | grep "Allow:" | cut -d' ' -f2-
