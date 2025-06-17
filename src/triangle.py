from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Triangle sides can't be less than 0")
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError("it is impossible to create a triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        """
        p - полупериметр,
        h - высота треугольника, проведенная к стороне side_a,
        :return: площадь треугольника
        """
        p = self.get_perimeter / 2
        h = (((p * (p-self.side_a) * (p-self.side_b) * (p-self.side_c)) ** 0.5) * 2) / self.side_a
        return int((self.side_a * h) / 2)
