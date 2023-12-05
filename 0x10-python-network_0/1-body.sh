#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

response=$(curl -s -w "%{http_code}" "$url")

status_code=${response: -3}

if [ "$status_code" -eq 200 ]; then
    # Extract and display the body of the response
    body=$(echo "$response" | sed '$ s/...$//')
    echo "Response Body:"
    echo "$body"
else
    echo "Error: Received status code $status_code"
fi
