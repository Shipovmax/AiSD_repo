'''
Опишите класс Circle, заданный радиусом.

Включите в описание класса методы:
вывода информации о круге на экран,
расчета длины окружности и площади круга,
и свойство, позволяющее установить цвет круга.
'''
import math


class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self._color = None

    def __str__(self) -> str:
        return f"Круг радиусом {self.radius}"

    def get_circumference(self) -> float:
        return 2 * math.pi * self.radius

    def get_area(self) -> float:
        return math.pi * (self.radius ** 2)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: str):
        self._color = value


my_circle = Circle(5)

print(my_circle)

print(f"Длина окружности: {round(my_circle.get_circumference(), 2)}")
print(f"Площадь круга: {round(my_circle.get_area(), 2)}")

my_circle.color = "Красный"
print(f"Цвет круга: {my_circle.color}")
