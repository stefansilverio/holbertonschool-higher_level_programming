#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if isinstance(a_dictionary, dict):
        if a_dictionary != None:
            try:
                del a_dictionary[key]
            except KeyError:
                return a_dictionary
            return a_dictionary
