import math

class Vehicle:
    def __init__(self: Vehicle, color: str):
        self._color = color

    @property
    def color(self: Vehicle) -> str:
        return self.__color

    @color.setter
    def _color(self:Vehicle, color: str):
        if isinstance(color, str) and len(color) > 0:
            self.__color = color
        else:
            self.__color = "White"

    def __str__(self: Vehicle):
        return f"Vehicle: color {self.color}"
    
class Auto(Vehicle):
    def __init__(self: Auto, color: str, make: str):
        super().__init__(color)
        self.make = make

    @property
    def make(self:Auto) -> str:
        return self.__make

    @make.setter
    def make(self: Auto, make: str):
        if isinstance(make, str) and len(make) > 0:
            self.__make = make
        else:
            self.__make = "Unknown"

    def __str__(self: Auto):
        return f"{super().__str__()}\n" + f"Auto: Make is {self.make}."

        
v1 = Vehicle("Red")
print(v1)
a1 = Auto("Green", "BMW")
print(a1)
