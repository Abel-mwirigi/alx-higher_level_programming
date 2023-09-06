#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """
    Represents a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
    Intializes an object rectangle
    """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getter for private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the private attribute width
        """
        if not isinstance(value, int):
            raise TypeError("width must bbe an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for the private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the private attribute height
        """
        if not isinstance(value, int):
            raise TypeError("height must bbe an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns perimeter
        """
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        returns a printable representation of the rectangle
         Represents the rectangle with the # character
       """

        if self.__width == 0 and self.__height == 0:
            return ("")

        s = []
        for i in range(self.__height):
            [s.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                s.append("\n")
        return ("".join(s))

    def __repr__(self):
        """returns a string representation"""
        shap = "Rectangle(" + str(self.__width)
        shap += ", " + str(self.__height) + ")"
        return shap

    def __del__(self):
        """
        indicates deletion of rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
