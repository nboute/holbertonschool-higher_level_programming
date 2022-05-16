#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print(f'{value:d}')
    except (TypeError, ValueError) as e:
        return False
    return True
