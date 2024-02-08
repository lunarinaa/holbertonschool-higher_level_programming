#!/usr/bin/python3
"""Defines a function"""

import json


def from_json_string(my_str):
    """Returns object represented by a JSON"""
    return json.loads(my_str)
