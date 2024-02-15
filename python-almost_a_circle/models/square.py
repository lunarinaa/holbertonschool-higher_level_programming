#!/usr/bin/python3
"""Defines a class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns user friendly representation of the square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Assigning argument to each attribute"""
        attributes = ['id', 'size', 'x', 'y']
        for i in range(len(args)):
            if i < len(attributes):
                setattr(self, attributes[i], args[i])
        for key, value in kwargs.items():
            if key in attributes:
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        return {'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
