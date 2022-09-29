import unittest
from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square

class TestFigures(unittest.TestCase):
    def test_rectangle(self):
        r = Rectangle(16, 16, 'синего')
        self.assertEqual(r.area(), 256)
        self.assertEqual(r.get_figure_type(), 'Прямоугольник')
        self.assertEqual(r.__repr__(), 'Прямоугольник синего цвета шириной 16 и высотой 16 площадью 256.')
    
    def test_circle(self):
        c = Circle(16, 'зеленого')
        self.assertEqual(c.area(), 804.247719318987)
        self.assertEqual(c.get_figure_type(), 'Круг')
        self.assertEqual(c.__repr__(), 'Круг зеленого цвета радиусом 16 площадью 804.247719318987.')

    def test_square(self):
        s = Square(16, 'красного')
        self.assertEqual(s.area(), 256)
        self.assertEqual(s.get_figure_type(), 'Квадрат')
        self.assertEqual(s.width, s.height)
        self.assertEqual(s.__repr__(), 'Квадрат красного цвета со стороной 16 площадью 256.')

if __name__ == '__main__':
    unittest.main(verbosity=2)