#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    a_dict = {'+': add, '-': sub, '/': div, '*': mul}

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if a_dict.get(sys.argv[2], 0) == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    x = int(sys.argv[1])
    y = int(sys.argv[3])

    print("{} {} {} = {}".format(x, sys.argv[2], y,
                                 a_dict[sys.argv[2]](x, y)))
