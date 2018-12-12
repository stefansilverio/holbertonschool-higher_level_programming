#!/usr/bin/python3
def multiple_returns(sentence):
    try:
        first = sentence[0]
    except IndexError:
        first = None
    length = len(sentence)
    return ((length, first))
