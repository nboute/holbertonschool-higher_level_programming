#!/usr/bin/python3

def safe_print_division(a, b):
    res = None
    try:
        res = a / b
    except ZeroDivisionError:
        pass
    finally:
        print(f'Inside result: {res}')
    return res
