'''
Создайте классы Окружность и Прямоугольник с методами подсчета периметра.

Выведите информацию, используя полиморфизм.
'''
import math


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __str__(self) -> str:
        return f"Окружность (Радиус: {self.radius}, Периметр: {self.get_perimeter():.2f})"


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        return f"Прямоугольник (Стороны: {self.width}x{self.height}, Периметр: {self.get_perimeter():.2f})"


shapes = [
    Circle(5.0),
    Rectangle(4.0, 6.0),
    Circle(3.5),
    Rectangle(10.0, 2.0)
]

print("=== ВЫВОД ИНФОРМАЦИИ ЧЕРЕЗ ПОЛИМОРФИЗМ ===")
for shape in shapes:
    print(shape)
