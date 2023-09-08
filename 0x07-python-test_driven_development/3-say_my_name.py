#!/usr/bin/python3
"""function that prints my name"""

def say_my_name(first_name, last_name=""):
    """Prints a statements with the first and last name variables
    Raises:
    TypeError: if either is not an integer"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
