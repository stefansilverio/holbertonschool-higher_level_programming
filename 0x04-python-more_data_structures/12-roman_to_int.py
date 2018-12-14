#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) == True or str == None:
        roman_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        val_list = []
        for i in roman_string:
            if i not in roman_dict.keys():
                return 0
            else:
                val_list.append(roman_dict.get(i))
        return(sum(val_list))
    else:
        return (0)
