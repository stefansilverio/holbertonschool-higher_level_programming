#!/usr/bin/python3
"""
This function prints out text
Returns:
text to stdout
"""


def text_indentation(text):
    """prints text to stdout
    Returns text
    """
    sym_list = ['.', ':', '?', ]
    string = ""
    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")
    for i in text:
        string = string + i
        if i in sym_list:
            string = string.strip()
            print(string)
            print()
            string = ""
    string = string.strip()
    print(string, end="")
