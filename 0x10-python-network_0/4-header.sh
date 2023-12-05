#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL
# and displays the body of the response

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

custom_header="X-School-User-Id: 98"

response_body=$(curl -s -H "$custom_header" "$url")

echo "Response Body:"
echo "$response_body"
