#!/usr/bin/python3
"""Defines class Mylist"""


class MyList(list):
    """Sorted printing"""

    def print_sorted(self):
        """Print list in ascending order"""
        print(sorted(self))
