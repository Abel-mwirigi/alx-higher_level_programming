#!/usr/bin/python3
"""program to create class rectangle that inherits from class base"""
from models.base import Base

class Rectangle(Base):
    """class rectangle that inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

   
    """getter and setter for width"""
    @property
    def width(self):
        """gets the value for width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """sets the value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.__width = value

    """getter and setter for height"""
    @property
    def height(self):
        """gets the value for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """sets the value for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        
        self.__height = value

    """getter and setter for x"""
    @property
    def x(self):
        """gets the value for x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """sets the value for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        
        if value < 0:
            raise ValueError("x must be >= 0")
        
        self.__x = value

    """getter and setter for y"""
    @property
    def y(self):
        """gets the value for y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """sets the value for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        
        if value < 0:
            raise ValueError("y must be >= 0")
        
        self.__y = value

    def area(self):
        """function to find area"""
        return self.__width * self.__height
    
    def display(self):
        """function to print the instance with the character #"""
        for k in range(self.__x):
            print()
        for i in range(self.__height):
            #for l in range(self.__y):
            print(" "*self.__y, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """A string representation of the class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,self.x, self.y,self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary represenation of a rectangle"""

        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
