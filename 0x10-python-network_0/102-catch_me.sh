#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me

response=$(curl -s -X PUT -L -d "user_id=98" "http://0.0.0.0:5000/catch_me" -w "\n%{http_code}")

status_code=$(echo "$response" | tail -n 1)

if [ "$status_code" -eq 200 ]; then
    response_body=$(echo "$response" | sed '$ d')
    printf "%s" "$response_body"
else
    echo "Error: Received status code $status_code"
fi
