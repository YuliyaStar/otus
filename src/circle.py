from src.figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('radius must be greater than 0')
        self.radius = radius

    @property
    def get_perimeter(self):
        return 2 * pi * self.radius

    @property
    def get_area(self):
        return pi * self.radius ** 2
