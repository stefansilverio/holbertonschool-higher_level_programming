#!/usr/bin/python3
def roman_to_int(roman_string):

    if isinstance(roman_string, str) is True or str == "None":

        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                      'D': 500, 'M': 1000}
        total = 0
        length = len(roman_string)
        for i in range(length):
            if i + 1 == length:
                total += roman_dict[roman_string[i]]
                return total
            elif roman_dict[roman_string[i + 1]] > roman_dict[roman_string[i]]:
                total += ((-1) * (roman_dict[roman_string[i]]))
            else:
                total += roman_dict[roman_string[i]]
        return total

    else:
        return 0
