#!/usr/bin/python3
# takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a paramete

import requests
import sys

q = sys.argv[1] if len(sys.argv) > 1 else ""

data = {'q': q}

try:
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    try:
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")

except requests.RequestException as e:
    print("Request error: {}".format(e))
