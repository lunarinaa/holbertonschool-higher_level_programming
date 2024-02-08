#!/usr/bin/python3
"""Defines function"""


def inherits_from(obj, a_class):
    """Returns true if the object is an inherited instance

    Args:
    obj - object
    a_class - class to match
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
