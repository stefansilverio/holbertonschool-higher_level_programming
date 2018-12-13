#!/usr/bin/python3
import calculator_1
import sys
if __name__ == "__main__":
    list = ['+', '-', '/', '%']
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i in list:
        if i == sys.argv[2]:
            print("{} {} {} = {}"
                  .format(int(sys.argv[1]),
                          sys.argv[2], int(sys.argv[3]),
                          int(sys.argv[1]) + int(sys.argv[3])))
            exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
