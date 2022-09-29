from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from art import *

def main():
    # У Вас в списке, где мы оставляем ссылки на репозитории, я 16-ый
    r = Rectangle(16, 16, 'синего')
    print(r)
    c = Circle(16, 'зеленого')
    print(c)
    s = Square(16, 'красного')
    print(s)
    art = text2art("KRAINIKOV RT5-31B", font='small')
    print(art)

if __name__ == "__main__":
    main()