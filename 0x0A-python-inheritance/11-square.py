#!/usr/bin/python3
"""11-square.py

This module contains a class Square that inherits
from Rectangle (9-rectangle.py):

Instantiation with size: def __init__(self, size)::
    - size must be private. No getter or setter
    - size must be a positive integer, validated by integer_validator

the area() method must be implemented

print() should print, and str() should return,
the square description: [Square] <width>/<height>
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        """Initializes a Square object when it is instanciated"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns area of the Square object"""
        return self.__size ** 2

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
