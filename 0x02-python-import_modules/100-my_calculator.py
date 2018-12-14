#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
import sys
if __name__ == "__main__":
    a_dict = {'+': add, '-': sub, '/': div, '*': mul}

    x = int(sys.argv[1])
    y = int(sys.argv[3])

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")

    elif a_dict.get(sys.argv[2], 0) == 0:
        print("Unknown operator. Available operators: +, -, * and /")

    else:
        print("{} {} {} = {}".format(x, sys.argv[2], y,
                                     a_dict[sys.argv[2]](x, y)))
