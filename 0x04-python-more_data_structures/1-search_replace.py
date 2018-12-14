#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if isinstance(my_list, list):
        my_list = [replace if i == search else i for i in my_list]
        return my_list
