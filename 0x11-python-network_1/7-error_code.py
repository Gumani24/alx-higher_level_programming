#!/usr/bin/python3
# takes in a URL, sends a request to the URL and displays the body of the response

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    content = response.text
    print(content)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))

except requests.RequestException as e:
    print("Request error: {}".format(e))
