#!/usr/bin/python3
"""Defines function"""


def write_file(filename="", text=""):
    """writes a striong to a text file"""
    count = 0
    with open(filename) as f:
        for c in f:
            count += 1
        return count
