#!/usr/bin/python3
import json
"""
write json
object to txt file
Return: none
"""


def save_to_json_file(my_obj, filename):
    """
    write json object to txt file
    """
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
