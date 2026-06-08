'''
Создайте класс ТРЕУГОЛЬНИК (две стороны и угол).
Реализуйте методы вычисления площади и периметра.
Дочерние классы: ПРЯМОУГОЛЬНЫЙ, РАВНОБЕДРЕННЫЙ, РАВНОСТОРОННИЙ.
'''

import math


class Triangle:
    def __init__(self, side_a: float, side_b: float, angle_deg: float):
        self.side_a = side_a
        self.side_b = side_b
        self.angle_rad = math.radians(angle_deg)

    def get_side_c(self) -> float:
        return math.sqrt(self.side_a ** 2 + self.side_b ** 2 - 2 * self.side_a * self.side_b * math.cos(self.angle_rad))

    def get_area(self) -> float:
        return 0.5 * self.side_a * self.side_b * math.sin(self.angle_rad)

    def get_perimeter(self) -> float:
        return self.side_a + self.side_b + self.get_side_c()

    def __str__(self):
        return (f"Тип: Общий треугольник\n"
                f"Стороны: a = {self.side_a:.2f}, b = {self.side_b:.2f}, c = {self.get_side_c():.2f}\n"
                f"Площадь: {self.get_area():.2f}\n"
                f"Периметр: {self.get_perimeter():.2f}")


class RightTriangle(Triangle):
    def __init__(self, leg_a: float, leg_b: float):
        super().__init__(leg_a, leg_b, 90.0)

    def __str__(self):
        return (f"Тип: Прямоугольный треугольник\n"
                f"Катеты: a = {self.side_a:.2f}, b = {self.side_b:.2f}\n"
                f"Гипотенуза: c = {self.get_side_c():.2f}\n"
                f"Площадь: {self.get_area():.2f}\n"
                f"Периметр: {self.get_perimeter():.2f}")


class IsoscelesTriangle(Triangle):
    def __init__(self, side: float, base: float, angle_between_them_deg: float):
        super().__init__(side, base, angle_between_them_deg)

    def __str__(self):
        return (f"Тип: Равнобедренный треугольник\n"
                f"Боковые стороны: {self.side_a:.2f}, Основание: {self.get_side_c():.2f}\n"
                f"Площадь: {self.get_area():.2f}\n"
                f"Периметр: {self.get_perimeter():.2f}")


class EquilateralTriangle(Triangle):
    def __init__(self, side: float):
        super().__init__(side, side, 60.0)

    def __str__(self):
        return (f"Тип: Равносторонний треугольник\n"
                f"Все стороны: {self.side_a:.2f}\n"
                f"Площадь: {self.get_area():.2f}\n"
                f"Периметр: {self.get_perimeter():.2f}")


t1 = RightTriangle(3.0, 4.0)
t2 = IsoscelesTriangle(5.0, 5.0, 45.0)
t3 = EquilateralTriangle(6.0)

print(t1)
print("-" * 40)
print(t2)
print("-" * 40)
print(t3)
