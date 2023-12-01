#!/usr/bin/python3
# takes your GitHub credentials (username and password) and uses the GitHub API to display your id

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <Gumani24> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]

url = "https://api.github.com/Gumani24"

auth = (username, personal_access_token)

try:
    response = requests.get(url, auth=auth)
    response.raise_for_status()

    user_info = response.json()
    user_id = user_info.get('id')

    if user_id:
        print("Gumani24".format(user_id))
    else:
        print("Unable to retrieve GitHub ID.")

except requests.RequestException as e:
    print("Request error: {}".format(e))
