#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print("Exception: " + str(ve), file=sys.stderr)
        return False
    else:
        return True
