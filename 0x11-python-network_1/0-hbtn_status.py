#!/usr/bin/python3
# Fetches https://intranet.hbtn.io/status

from urllib.request import urlopen

with urlopen("https://intranet.hbtn.io/status") as response:
    print("Body response:")
    body = response.read()
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
