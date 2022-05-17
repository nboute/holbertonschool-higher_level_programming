#!/usr/bin/python3
"""6-square.py

This module contains a class Square that defines a square by:
(based on 5-square.py)

- Private instance attribute: size:

    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:

        - size must be an integer, otherwise raise a TypeError exception
          with the message 'size must be an integer'
        - if size is less than 0, raise a ValueError exception
          with the message 'size must be >= 0'

- Private instance attribute: position:
    - property def position(self): to retrieve it
    - property setter def position(self, value): to set it:

        - position must be a tuple of 2 positive integers,
          otherwise raise a TypeError exception with the message
          'position must be a tuple of 2 positive integers'

- Instantiation with optional size: def __init__(self, size=0):

- Public instance method:
    def area(self): that returns the current square area

-Public instance method:
    def my_print(self): that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
"""


class Square():
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Sets attributes for a Square object when it is instanciated

            Args:
                size (int): Size of all sides of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (type(position) is not tuple
                or all(type(n) is int for n in position) is False):
            raise TypeError("position must be a tuple of 2 positive"
                            " integers")
        self.__position = position

    @property
    def size(self):
        """property method

        Returns:
            (int) - Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method

        Args:
            value (int): Size to set for the square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the square area of the Square object

        Returns:
            (int) - Square area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints square to stdout"""
        if self.__size == 0:
            print()
            return
        for a in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(' ', end="")
            for j in range(self.__size):
                print('#', end='')
            print()

    @property
    def position(self):
        """property method

        Returns:
            (int) - position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter method

        Args:
            value (tuple): position to set for the square.
        """
        if (type(value) is not tuple or len(value) != 2
                or all(type(n) is int for n in value) is False):
            raise TypeError("position must be a tuple of 2 positive"
                            " integers")
        self.__position = value
