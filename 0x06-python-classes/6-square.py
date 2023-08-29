#!/usr/bin/python3
"""Defining a class square"""

class Square:
    def __init__(self, size=0, position=(0, 0)):
        """initializes a square
        Args:
        size(int):size of the square
        position (int, int): the position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
         """returns the position"""
         return self.__position
    
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of square"""
        return self.__size ** 2
    
    def my_print(self):
         """print # square"""
         if self.__size == 0:
            print()
         else:
            for _ in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
