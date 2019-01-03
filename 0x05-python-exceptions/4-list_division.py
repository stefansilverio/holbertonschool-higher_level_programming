#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    idx = quotient = 0
    new_list = []
    while list_length > idx:
        quotient = 0
        try:
            quotient = my_list_1[idx] / my_list_2[idx]
        except (ZeroDivisionError, TypeError):
            if my_list_2[idx] == 0:
                print("division by 0")
            else:
                print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(quotient)
            idx += 1
    return new_list
