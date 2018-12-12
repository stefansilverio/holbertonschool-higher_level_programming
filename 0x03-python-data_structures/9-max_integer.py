#!/usr/bin/python3
def max_integer(my_list=[]):
    try:
        biggest = my_list[0]
    except IndexError:
        biggest = None
        return biggest
    for i in my_list:
        if i > biggest:
            biggest = i
    return biggest
