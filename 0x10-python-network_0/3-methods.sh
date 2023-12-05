#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

allowed_methods=$(curl -s -i -X OPTIONS "$url" | awk -F': ' '/Allow/ {print $2}' | tr -d '\r')

echo "Allowed HTTP Methods for $url: $allowed_methods"
