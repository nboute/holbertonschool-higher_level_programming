#!/usr/bin/python3
"""101-add_attribute.py

This module contains a function that adds a new attribute to an object
    if it’s possible:

Raise a TypeError exception, with the message 'can't add new attribute'
    if the object can’t have new attribute

"""


def add_attribute(obj, name, value):
    """Adds attribute to an object if possible, otherwise raises exception"""
    if (hasattr(obj, __dict__) is False):
        raise AttributeError("can't add new attribute")
    setattr(obj, name, value)

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
