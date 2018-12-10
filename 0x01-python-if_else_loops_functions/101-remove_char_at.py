#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    if n >= 0 and n < length:
        str2 = str.replace(str[n], "")
        print("{0}".format(str2), end='')
    else:
        print("{}".format(str), end='')
    return ('')
