#!/usr/bin/python3

"""103-magic_class.py

This module contains a class MagicClass that defines a circle,
corresponding to a specific bytecode
"""

import math


class MagicClass():
    """Defines a circle"""

    def __init__(self, radius=0):
        """Initalizes a MagicClass object when instantiated"""
        self._MagicClass__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Returns area of MagicClass object"""
        return self._MagicClass__radius ** 2 * math.pi()

    def circumference(self):
        """Returns circumference of MagicClass object"""
        return 2 * math.pi * self._MagicClass__radius
