#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    return list(map(lambda number: (True, False)[number & 1], my_list))
