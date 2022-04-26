#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        c = str[i]
        if (ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z')):
            c = chr(ord(str[i]) - ord('a') + ord('A'))
        print('{}'.format(c), end='')
    print('')
