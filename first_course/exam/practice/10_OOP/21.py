'''
Создайте родительский класс Прямоугольник (площадь, периметр) и дочерний класс Квадрат.
'''


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __str__(self):
        return (f"Фигура: Прямоугольник ({self.width}x{self.height})\n"
                f"Площадь: {self.get_area():.2f}\n"
                f"Периметр: {self.get_perimeter():.2f}\n"
                f"{'-' * 30}")


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return (f"Фигура: Квадрат (Сторона: {self.side})\n"
                f"Площадь: {self.get_area():.2f}\n"
                f"Периметр: {self.get_perimeter():.2f}\n"
                f"{'-' * 30}")


rect = Rectangle(4.0, 6.0)
square = Square(5.0)

print(rect)
print(square)
