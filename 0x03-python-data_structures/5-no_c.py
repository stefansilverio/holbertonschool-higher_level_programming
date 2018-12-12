#!/usr/bin/python3
def no_c(my_string):
    idx = 0
    for i in my_string:
        if i is 'c' or i is 'C':
            my_string = my_string[:idx] + my_string[idx + 1:]
        if i is 'c' or i is 'C':
            continue
        idx += 1
    return my_string
