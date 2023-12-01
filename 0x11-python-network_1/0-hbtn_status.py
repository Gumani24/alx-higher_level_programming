#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print("- Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
except urllib.error.URLError as e:
    print("Error: {}".format(e.reason))
