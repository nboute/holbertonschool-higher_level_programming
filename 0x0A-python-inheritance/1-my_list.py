#!/usr/bin/python3
"""1-my_list.py
This module contains a class MyList that inherits from list
"""


class MyList(list):
    """MyList - Subclass of list"""

    def __init_subclass__(cls):
        """Sets attributes for a Mylist object

            Calls super function to init like a list does
        """

        return super().__init_subclass__()

    def print_sorted(self):
        """Prints itself, sorted by ascending order"""

        print(sorted(self))
