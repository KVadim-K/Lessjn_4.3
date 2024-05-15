# Задача №2 с использованием полиморфизма.
# Продемонстрировать принцип полиморфизма через реализацию разных классов, представляющих геометрические формы, и метод для расчёта площади каждой формы.
# Создать базовый класс Shape с методом area(), который просто возвращает 0.
# Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square), каждый из которых переопределяет метод area().
# В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры. Написать функцию, которая принимает объект класса Shape и выводит его площадь.

class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius # Привязка к радиусу
    def area(self):
        return 3.14 * self.radius * self.radius # Площадь круга можно
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
def print_Area(shape):
    print(f"Площадь фигуры = {shape.area()}")

circle = Circle(5)
print_Area(circle)
squere = Square(8)
print_Area(squere)
rectangle = Rectangle(5, 10)
print_Area(rectangle)