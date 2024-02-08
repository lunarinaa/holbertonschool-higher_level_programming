#!/usr/bin/python3
"""Defines a function"""


def read_file(filename=""):
    """Reads the text file and prints its content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
