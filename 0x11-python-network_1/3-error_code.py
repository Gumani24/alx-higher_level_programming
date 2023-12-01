#!/usr/bin/python3
# takes in a URL, sends a request to the URL and displays the body of the response

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print(content)
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
except urllib.error.URLError as e:
    print("URLError: {}".format(e.reason))
