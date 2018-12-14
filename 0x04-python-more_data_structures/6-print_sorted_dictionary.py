#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if isinstance(a_dictionary, dict):
        if a_dictionary is not None:
            for key, value in sorted(a_dictionary.items()):
                print("{}: {}".format(key, value))
