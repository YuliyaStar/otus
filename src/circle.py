import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Invalid value")
        self.radius = radius

    @property
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    @property
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
