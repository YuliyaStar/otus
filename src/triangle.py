import math
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Triangle sides can't be less than 0")
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError("It is impossible to create a triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return round(self.side_a + self.side_b + self.side_c, 2)

    @property
    def area(self):
        h = self.perimeter / 2
        return round(math.sqrt((h * (h-self.side_a) * (h-self.side_b) * (h-self.side_c))), 2)
