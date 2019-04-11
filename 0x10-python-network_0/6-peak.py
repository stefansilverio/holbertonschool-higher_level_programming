#!/usr/bin/python3
# find the peak in a list of numbers


def find_peak(list_of_integers):
    if isinstance(list_of_integers, list) is false:
        return None
    if list_of_integers is None or len(list_of_integers) is 0:
        return None
    if len(list_of_integers) is 1:
        return list_of_integers[0]
    leng = len(list_of_integers)
    mid = int(leng / 2)
    if len(list_of_integers) is 2:
        if list_of_integers[mid - 1] <= list_of_integers[mid]:
            return list_of_integers[mid]
        return list_of_integers[mid - 1]
    if list_of_integers[mid - 1] > list_of_integers[mid] and\
       list_of_integers[mid + 1] > list_of_integers[mid]:
        return list_of_integers[mid]
    if list_of_integers[mid - 1] > list_of_integers[mid]:
        left_list = []
        left_list = list_of_integers[:mid + 1]
        return find_peak(left_list)
    else:
        right_list = []
        right_list = list_of_integers[mid:]
        return find_peak(right_list)
