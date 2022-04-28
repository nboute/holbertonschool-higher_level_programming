#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import string
    names = dir(hidden_4)
    for name in names:
        if name.startswith("__") is False:
            print(f'{name}')
