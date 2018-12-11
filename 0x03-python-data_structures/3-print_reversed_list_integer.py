#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list) == False:
        print("not a list")
    my_list = my_list[::-1]
    for i in my_list:
        print("{:d}".format(i))
