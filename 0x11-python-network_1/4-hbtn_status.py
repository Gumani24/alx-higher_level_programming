#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status

import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    content = response.text
    print("- Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

except requests.HTTPError as e:
    print("Error code: {}".format(e.response.status_code))
except requests.RequestException as e:
    print("Request error: {}".format(e))
