#!/usr/bin/python3
"""this module implemets inheritance via importing the class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This Rectangle class is inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initializing a new recatangle with width and height"""
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to find the area of the rectangle belonging
        to this class(Rectangle)"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of a rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
