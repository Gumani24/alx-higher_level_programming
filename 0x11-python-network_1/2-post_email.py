#!/usr/bin/python3
# takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter
# and displays the body of the response

import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    with urllib.request.urlopen(url, data=data) as response:
        content = response.read().decode('utf-8')
        print(content)
except urllib.error.HTTPError as e:
    print("HTTPError: {}".format(e))
except urllib.error.URLError as e:
    print("URLError: {}".format(e))
