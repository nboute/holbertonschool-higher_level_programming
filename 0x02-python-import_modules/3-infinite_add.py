#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb = 0
    for i in range(len(sys.argv) - 1):
        nb += int(sys.argv[i + 1])
    print(f'{nb}')
