#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dic = dict(sorted(a_dictionary.items()))
    for elem in sorted_dic:
        print(f'{elem}: {sorted_dic[elem]}')
