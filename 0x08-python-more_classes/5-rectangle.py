#!/usr/bin/python3
"""5-rectangle.py

This module contains a class Rectangle that defines a rectangle by:
(based on 4-rectangle.py)


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

Public instance method: def area(self):
    that returns the rectangle area

Public instance method: def perimeter(self):
    that returns the rectangle perimeter:

    if width or height is equal to 0, perimeter is equal to 0

print() and str() should print the rectangle with the character #:
    if width or height is equal to 0, return an empty string
repr() should return a string representation of the rectangle to be able to
    recreate a new instance by using eval() (see example below)

Print the message Bye rectangle... (... being 3 dots not ellipsis) when an
instance of Rectangle is deleted
"""


class Rectangle():
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """_init_ -- initialization method

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
            __width: Private instance attribute: Width of rectangle
            __height: Private instance attribute: Height of rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get area of rectangle

        Returns:
            int: area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Get perimeter of rectangle

        Returns:
            int: perimeter of rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        """String representation of rectangle

        Returns:
            string: rectangle in string format using character '#'
        """
        s = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                s += '#'
            s += '\n'
        return s[:-1]

    def __repr__(self):
        """string representation of the rectangle to recreate the same instance
           using eval()
            string: "Rectangle(width, height)
        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Prints string when an instance of the class is deleted"""
        print("Bye rectangle...")
