#!/usr/bin/python3
""" function to add two integers """

def add_integer(a, b=98):
    """Returns sum of a and b
    Raises:
    TypeError:if a and b are not integer or float"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
