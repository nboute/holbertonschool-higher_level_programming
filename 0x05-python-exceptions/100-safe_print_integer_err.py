#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print(f'{value:d}')
        return True
    except Exception as e:
        sys.stderr.write(f'Exception: {e}\n')
        return False