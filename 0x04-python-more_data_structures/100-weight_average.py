#!/usr/bin/python3

def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    sum = 0
    div = 0
    for elem in my_list:
        sum += elem[0] * elem[1]
        div += elem[1]
    return sum / div
