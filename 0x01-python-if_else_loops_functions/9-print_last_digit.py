#!/usr/bin/python3
def print_last_digit(number):
    if (type(number) != int):
        raise TypeError
    digit = repr(number)[-1]
    print('{}'.format(digit), end='')
    return digit
