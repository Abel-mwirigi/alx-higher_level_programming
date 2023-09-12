#!/usr/bin/python3
"""A text file reading funtion"""


def read_file(filename=""):
    """Prints the contents of a UTF* text file to stdout"""
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end='')
