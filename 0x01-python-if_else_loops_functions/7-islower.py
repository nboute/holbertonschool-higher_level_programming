#!/usr/bin/python3
from xml.dom.minidom import TypeInfo


def islower(c):
    if (c >= 'a' and c <= 'z'):
        return True
    elif (c < ' '):
       raise TypeError
    else:
        return False
