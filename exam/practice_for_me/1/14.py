"""
Создайте класс Квадрат.

Координаты верхнего левого угла и длина стороны должны быть приватными атрибутами.

Реализуйте метод, который "рисует" закрашенный квадрат в консоли (символами, например, *),
а также методы изменения размера и валидации координат при попытке их обновления.
"""


class Square:
    def __init__(self, x: int, y: int, side: int):
        self.__x = 0
        self.__y = 0
        self.__side = 1

        self.set_coordinates(x, y)
        self.set_side(side)

    def set_coordinates(self, x: int, y: int):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Координаты должны быть целыми числами")
        if x < 0 or y < 0:
            raise ValueError("Координаты не могут быть отрицательными")
        self.__x = x
        self.__y = y

    def set_side(self, side: int):
        if not isinstance(side, int):
            raise TypeError("Длина стороны должна быть целым числом")
        if side <= 0:
            raise ValueError("Длина стороны должна быть больше нуля")
        self.__side = side

    def get_coordinates(self) -> tuple:
        return self.__x, self.__y

    def get_side(self) -> int:
        return self.__side

    def draw(self):
        for _ in range(self.__y):
            print()
        for _ in range(self.__side):
            print(" " * self.__x + "*" * self.__side)
