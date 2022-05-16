#!/usr/bin/python3

from typing import Type


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            new_list.append(res)
    return new_list