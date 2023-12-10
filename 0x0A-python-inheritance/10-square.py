#!/usr/bin/python3
"""
contains class Square
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ class square that inherits from Rectangle"""
    def __init__(self, size):
        """ initialize class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ finds area """
        return self.__size ** 2
