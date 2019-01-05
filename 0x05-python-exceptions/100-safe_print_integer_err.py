#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print("Exception: " + str(ve), file=sys.stderr)
        return False
    except TypeError as te:
        print("Exception: " + str(te), file=sys.stderr)
        return False
    else:
        return True
