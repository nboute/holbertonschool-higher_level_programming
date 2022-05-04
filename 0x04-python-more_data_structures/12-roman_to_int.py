#!/usr/bin/python3

def roman_to_int(roman_string):
    if (isinstance(roman_string, str) is False or len(roman_string) == 0):
        return 0
    my_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
               'I': 1, 'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9,
               'IV': 4}
    number = 0
    i = 0
    while i in range(len(roman_string)):
        if (i + 1 < len(roman_string) and roman_string[i: i + 2] in my_dict):
            number += my_dict[roman_string[i: i + 2]]
            i += 2
        else:
            number += my_dict[roman_string[i]]
            i += 1
    if (isinstance(number, int) is True):
        return number
    return 0
