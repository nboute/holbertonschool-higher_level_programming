#!/usr/bin/python3
"""7-base_geometry.py

This module contains a class BaseGeometry (based on 6-base_geometry.py):

    - Public instance method: def area(self):
        that raises an Exception with the message 'area() is not implemented'
    - Public instance method: def integer_validator(self, name, value):
            that validates value:
        you can assume name is always a string

        - if value is not an integer: raise a TypeError exception,
            with the message '<name> must be an integer'
        - if value is less or equal to 0: raise a ValueError exception
            with the message '<name> must be greater than 0'
"""


class BaseGeometry():
    """Base geometry methods/atributes"""
    def __init__(self):
        """ Sets attributes for a BaseGeometry object when it's instanciated"""
        pass

    def area(self):
        """Method to get area of an object. Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if given integer has valid type and value"""
        if (isinstance(value, int) is False):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
