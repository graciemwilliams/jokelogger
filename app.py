#!/usr/bin/python3

import requests
import json
import logging

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
response = json.loads(response.text)

# calling the key out from within this payload
id = response['id']
setup = response['setup']
punchline = response['punchline']

print(id, setup, punchline)

