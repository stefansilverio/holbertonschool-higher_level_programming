#!/usr/bin/python3
def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        my_set = set(my_list)
        return sum(my_set)
