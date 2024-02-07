#!/usr/bin/python3
"""Defines function"""


def is_same_class(obj, a_class):
    """Returns true if the object is instance of the specified class"""
    if type(obj) == a_class:
        return True
    return False
