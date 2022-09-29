from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color()
        self.color.colorproperty = color

    def area(self):
        return self.width * self.height

    def get_figure_type(self):
        return self.FIGURE_TYPE

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            self.get_figure_type(),
            self.color.colorproperty,
            self.width,
            self.height,
            self.area()
        )