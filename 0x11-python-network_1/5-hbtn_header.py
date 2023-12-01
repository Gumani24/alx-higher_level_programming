#!/usr/bin/python3
# takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response heade

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")

except requests.HTTPError as e:
    print("Error code: {}".format(e.response.status_code))
except requests.RequestException as e:
    print("Request error: {}".format(e))
