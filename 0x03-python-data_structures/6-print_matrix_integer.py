#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if i != 0:
            print('')
        for j in range(len(matrix[i])):
            if j != 0:
                print(' ', end='')
            print(f'{matrix[i][j]}', end='')
    print('')
