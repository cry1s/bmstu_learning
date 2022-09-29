from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math

class Circle(Figure):
    FIGURE_TYPE = "Круг"
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color()
        self.color.colorproperty = color

    def get_figure_type(self):
        return self.FIGURE_TYPE
    
    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            self.get_figure_type(),
            self.color.colorproperty,
            self.radius,
            self.area()
        )