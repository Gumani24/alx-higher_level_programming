#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and displays the body of the response

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
email="test@gmail.com"
subject="I will always be here for PLD"

response_body=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")

echo "Response Body:"
echo "$response_body"
