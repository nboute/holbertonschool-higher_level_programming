#!/usr/bin/python3
"""Square inherits from Rectangle which inherits from BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


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

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
