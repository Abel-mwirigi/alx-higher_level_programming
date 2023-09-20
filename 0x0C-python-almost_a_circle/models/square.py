#!/usr/bin/python3
"""A Square Class that inherits from Rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """square class that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """calling the super class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the value of size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """sets the value for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns the string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,self.y, self.width)
    
    def to_dictionary(self):
        """Returns a dictionary representation of the square"""
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}
    