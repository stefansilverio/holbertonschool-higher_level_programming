#!/usr/bin/python3
"""
This function prints a square of hashes
Returns:
Hash
"""


def print_square(size):
    """Prints a square of hashes
    Returns hashes
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif isinstance(size, int) is not True:
        raise TypeError("size must be an integer")
    elif size < 0:
            raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
