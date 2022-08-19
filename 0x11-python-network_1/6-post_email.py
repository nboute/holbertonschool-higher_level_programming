#!/usr/bin/python3
"""Post given email as parameter to given url"""
import requests
from sys import argv

r = requests.post(argv[1], data={'email': argv[2]})
print(r.text)
