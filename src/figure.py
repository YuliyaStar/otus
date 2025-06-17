from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def get_area(self):
        pass

    @property
    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Should be a Figure")
        return self.get_area() + figure.get_area()
