import math
from abc import ABC, abstractmethod

class Shape(ABC):
     @abstractmethod
     def area(self: Shape):
          pass

class Rectangle(Shape):
    def __init__(self: Rectangle, length: int = 0, width: int= 0):
        self._length = length
        self._width = width

    #Getter
    @property
    def length(self:Rectangle) -> int:
        return self._length

    @length.setter
    def length(self:Rectangle, length: int):
        if isinstance(length, int) and length > 0:
            self._length = length
        else:
            raise ValueError("Length must be positive number")

    @property
    def width(self:Rectangle) -> int:
            return self._width
    
    @width.setter
    def width(self:Rectangle, width: int):
            if isinstance(width, int) and width > 0:
                self._width = width
            else:
                raise ValueError("Width must be positive number")

    def __str__(self: Rectangle) -> str:
         return f"Rectangle length : {self._length}, width: {self._width}."

    @property
    def area(self: Rectangle) -> int:
         return self._length * self._width

class Square(Rectangle):
    def __init__(self: Square, side: int = 0):
          super().__init__(side, side)
          self._is_square = True

    @property
    def is_square(self: Square) -> bool:
         return self._is_square

class Circle(Shape):
    def __init__(self: Circle, radius: int):
        self.radius = radius

    @property
    def radius(self:Circle) -> int:
        return self.__radius

    @radius.setter
    def radius(self:Circle, radius: int):
        if isinstance(radius, int) and radius > 0:
            self.__radius = radius
        else:
            raise ValueError("Radius must be positive number")

    @property
    def area(self: Circle):
        return (self.__radius ** 2) * math.pi


def print_area(obj: Shape):
    print(f"Area of {type(obj)} is {obj.area}")



r1 = Rectangle(5,6)
print_area(r1)

s1 = Square(10)
print_area(s1)

c1 = Circle(7)
print_area(c1)

