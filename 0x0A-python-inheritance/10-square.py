#!/usr/bin/python3

Rectangle = __import__("9-rectangle").Rectangle

"""10-square.py

This module contains a class Square that inherits
from Rectangle (9-rectangle.py):

Instantiation with size: def __init__(self, size)::
    - size must be private. No getter or setter
    - size must be a positive integer, validated by integer_validator

the area() method must be implemented
"""


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        """Initializes a Square object when it is instanciated"""
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area of the Square object"""
        return self.__size ** 2
