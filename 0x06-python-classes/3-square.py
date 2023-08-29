#!/usr/bin/python3

"""Defining a class square"""

class Square:
    """Represents a square
    Attributes:
    __size (int): size of the square"""
    def __init__(self, size=0):
        """Represents a square
    Attributes:
    __size (int): size of the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the square's area
        Returns:
            The area of the square"""
        return self.__size ** 2

