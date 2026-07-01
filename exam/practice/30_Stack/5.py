'''
Реализуйте класс Стек (через list).
Поменяйте местами первый и последний элементы.
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

    def swap_first_and_last(self):
        if self.size() < 2:
            return

        temp_items = []
        while not self.is_empty():
            temp_items.append(self.pop())

        temp_items[0], temp_items[-1] = temp_items[-1], temp_items[0]

        for item in reversed(temp_items):
            self.push(item)
