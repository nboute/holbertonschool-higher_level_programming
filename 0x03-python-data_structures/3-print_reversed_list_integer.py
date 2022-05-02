#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for elem in reversed(range(len(my_list))):
        print(f'{my_list[elem]:d}')
