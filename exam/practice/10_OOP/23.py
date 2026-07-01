'''
Создайте класс Квадрат, который рисует закрашенный квадрат (координаты верхнего левого угла и длина стороны — приватные).
'''


class Square:
    def __init__(self, x: int, y: int, side: int):
        self.__x = x
        self.__y = y
        self.__side = side

    def draw(self):
        if self.__side <= 0:
            return

        for _ in range(self.__side):
            print("*" * self.__side)


square = Square(x=0, y=0, side=5)
square.draw()
