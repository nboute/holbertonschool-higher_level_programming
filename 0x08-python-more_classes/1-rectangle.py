#!/usr/bin/python3
"""1-rectangle.py

This module contains a class Rectangle that defines a rectangle by:
(based on 1-rectangle.py)


Private instance attribute: width:

- property def width(self): to retrieve it
- property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception
    with the message 'width must be an integer'
if width is less than 0,
    raise a ValueError exception with the `message width must be >= 0`

Private instance attribute: height:
property def height(self): to retrieve it

property setter def height(self, value): to set it:

height must be an integer, otherwise raise a TypeError exception
with the message 'height must be an integer'

if height is less than 0, raise a ValueError exception
with the message 'height must be >= 0'

Instantiation with optional width and height:
    def __init__(self, width=0, height=0):

"""


class Rectangle():
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """_init_ -- initialization method

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
            __width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter for width

        Returns:
            int: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width:

        Args:
            value (int): width to set for rectangle

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height

        Returns:
            int: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for heigth:

        Args:
            value (int): height to set for rectangle

        """
        if type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
