#!/usr/bin/python3
# takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
except urllib.error.HTTPError as e:
    print("HTTPError: {}".format(e))
except urllib.error.URLError as e:
    print("URLError: {}".format(e))
