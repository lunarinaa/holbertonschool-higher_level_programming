#!/usr/bin/python3
"""Defines a function"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure"""
    return obj.__dict__
