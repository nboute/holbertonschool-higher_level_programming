#!/usr/bin/python3

import sys


def can_place(matrix, size, y, x):
    """Checks if we can place a queen at the position x, y on the chessboard"""
    for i in range(size):
        if i != x and matrix[y][i] is True:
            return False
        if i != y and matrix[i][x] is True:
            return False
    i = y - 1
    j = x - 1
    while i >= 0 and j >= 0:
        if matrix[i][j] is True:
            return False
        i -= 1
        j -= 1

    i = y + 1
    j = x - 1
    while i < size and j >= 0:
        if matrix[i][j] is True:
            return False
        i += 1
        j -= 1

    i = y - 1
    j = x + 1
    while i >= 0 and j < size:
        if matrix[i][j] is True:
            return False
        i -= 1
        j += 1

    i = y + 1
    j = x + 1
    while i < size and j < size:
        if matrix[i][j] is True:
            return False
        i += 1
        j += 1
    return True


def print_queens(matrix, size):
    """prints a valid solution of the nqueens problem"""
    count = 0
    print('[', end='')
    for i in range(size):
        for j in range(size):
            if matrix[i][j] is True:
                if count != 0:
                    print(", ", end='')
                print(f'[{i}, {j}]', end='')
                count = 1
    print(']')


def nqueens(matrix, size, y):
    """Recursive function that prints all solutions of nqueens problem
        with size=n"""
    if (y == size):
        print_queens(matrix, size)
        return
    for x in range(size):
        if can_place(matrix.copy(), size, y, x) is True:
            matrix[y][x] = True
            nqueens(matrix, size, y + 1)
            matrix[y][x] = False
    return


if len(sys.argv) != 2:
    print("Usage: nqueens Nss")
    exit(1)
try:
    size = int(sys.argv[1])
except (TypeError, ValueError):
    print("N must be a number")
    exit(1)

if size < 4:
    print("N must be at least 4")
    exit(1)


matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(False)
    matrix.append(row)

nqueens(matrix, size, 0)
