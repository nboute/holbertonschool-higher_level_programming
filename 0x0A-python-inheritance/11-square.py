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
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square. Inherits from Rectangle class"""

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Magic method to print square description
        """

        return "[Square] {}/{}".format(self.__size, self.__size)
