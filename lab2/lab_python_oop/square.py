from lab_python_oop.rectangle import Rectangle
from lab_python_oop.color import Color

class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def get_figure_type(self):
        return self.FIGURE_TYPE

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            self.get_figure_type(),
            self.color.colorproperty,
            self.width,
            self.area()
        )