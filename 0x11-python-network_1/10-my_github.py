#!/usr/bin/python3
# Uses github credentials to get id of user, using github API
from sys import argv
import requests

try:
    resp = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(resp.json()['id'])
except Exception as e:
    print('None')
