#!/usr/bin/python3
"""Defines function"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is instance of or inherited"""
    if isinstance(obj, a_class):
        return True
    return False
