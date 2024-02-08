#!/usr/bin/python3
"""Defines function"""


def append_write(filename="", text=""):
    """Appends a string at the end"""
    with open(filename, "a", encoding="utf8") as f:
        return f.write(text)
