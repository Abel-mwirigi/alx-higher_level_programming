#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """
    Representation of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize an object rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        getter for the private  attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the private  attribute width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width nust be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for the private  attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the private  attribute height
        """
        if not isinstance(value, int):
            raise TypeError("height nust be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculates the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculates the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        prints a representation of the rectangle
        """
        s = ""
        if self.__width != 0 and self.__height != 0:
            s += "\n".join("#" * self.__width for i in range(self.__height))
        return s
