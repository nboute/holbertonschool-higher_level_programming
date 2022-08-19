#!/usr/bin/env python3
# Display body of given url, or error code if there is an error
from urllib import request, error
from sys import argv

try:
    with request.urlopen(argv[1]) as response:
        print(response.read().decode('utf-8'))
except error.HTTPError as exception:
    print('Error code: {}'.format(exception.code))
