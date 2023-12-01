#!/usr/bin/python3
# takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter
# and finally displays the body of the response

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Prepare data to be sent in the POST request
data = {'email': email}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    content = response.text
    print(content)

except requests.HTTPError as e:
    print("Error code: {}".format(e.response.status_code))
except requests.RequestException as e:
    print("Request error: {}".format(e))
