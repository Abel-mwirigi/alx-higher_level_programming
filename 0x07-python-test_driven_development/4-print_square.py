#!/usr/bin/python3
"""Prints a square using the hash symbol"""

def print_square(size):
    """prints a square of '#' it size is passed to the function

    Raises:
    TypeError: if size is not an integer
    ValueError: if value of size is less than zero"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
