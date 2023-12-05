#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

url=$1
json_file=$2

response_body=$(curl -s -X POST -d "@$json_file" -H "Content-Type: application/json" "$url")

echo "Response Body:"
echo "$response_body"
