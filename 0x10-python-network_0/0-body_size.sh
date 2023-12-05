#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

response_body=$(curl -sI "$url" | awk '/Content-Length/ {print $2}' | tr -d '\r')

if [ -z "$response_body" ]; then
    echo "Error: Content-Length not found in the response headers"
    exit 1
fi

echo "Size of the response body: ${response_body} bytes"
