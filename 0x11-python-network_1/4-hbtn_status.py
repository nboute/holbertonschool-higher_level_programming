#!/usr/bin/python3
# Fetches https://intranet.hbtn.io/status
import requests

resp = requests.get("https://intranet.hbtn.io/status")

print('Body response:')
print('\t- type: {}'.format(type(resp.text)))
print('\t- content: {}'.format(resp.text))
