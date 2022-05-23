#!/usr/bin/python3
"""Rectangle - Class that defines a rectangle"""


class Rectangle:

    def __init__(self, width=0, height=0):
        """_init_ -- initialization method

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
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
        if type(value) != int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
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
        if type(value) != int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value
