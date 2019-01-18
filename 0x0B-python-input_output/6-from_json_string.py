#!/usr/bin/python3
import json
"""
deserialize object
Return:
new object
"""


def from_json_string(my_str):
    """
    Return new object
    """
    return json.loads(my_str)
