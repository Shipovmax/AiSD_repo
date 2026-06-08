'''
Реализуйте класс Стек.
Удалите из него все элементы, которые не являются квадратами целых чисел.
'''


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        raise IndexError("Попытка извлечь элемент из пустого стека")

    def peek(self):
        if not self.is_empty():
            return self.__items[-1]
        return None

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    def get_all_items(self):
        return self.__items.copy()

    def filter_perfect_squares(self):
        import math

        valid_items = []
        while not self.is_empty():
            item = self.pop()
            if item >= 0:
                root = int(math.isqrt(item))
                if root * root == item:
                    valid_items.append(item)

        for item in reversed(valid_items):
            self.push(item)
