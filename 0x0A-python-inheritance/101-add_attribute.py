#!/usr/bin/python3
"""101-add_attribute.py

This module contains a function that adds a new attribute to an object
    if it’s possible:

Raise a TypeError exception, with the message 'can't add new attribute'
    if the object can’t have new attribute

"""


def add_attribute(obj, name, value):
    if (hasattr(obj, __dict__) is False):
        raise AttributeError("can't add new attribute")
    setattr(obj, name, value)
