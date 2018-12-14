#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):
        if a_dictionary != None:
            new_dict = a_dictionary.copy()
            [new_dict.update((x, y*2) for x, y in new_dict.items())]
        return new_dict
