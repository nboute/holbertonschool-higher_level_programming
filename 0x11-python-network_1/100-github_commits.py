#!/usr/bin/python3
"""Lists 10 latest commits of given repository"""
from sys import argv
import requests

url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
resp = requests.get(url)
for index, elem in enumerate(resp.json()):
    print('{}: {}'.format(elem.get('sha'),
          elem.get('commit').get('author').get('name')))
    if index == 10:
        break
