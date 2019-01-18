#!/usr/bin/python3
import json
"""
create pyobject from
json file
Return: none
"""


def load_from_json_file(filename):
    """
    create pyobject
    """
    with open(filename) as f:
        return json.load(f)
