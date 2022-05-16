#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = None
    try:
        res = fct(args[0], args[1])
        return res
    except Exception as e:
        sys.stderr.write(f'Exception: {e}\n')
        return None
