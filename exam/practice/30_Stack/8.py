'''
Реализуйте класс Стек.
Найдите минимальный элемент и вставьте после него 0.
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

    def insert_zero_after_min(self):
        if self.is_empty():
            return

        temp_items = []
        while not self.is_empty():
            temp_items.append(self.pop())

        temp_items.reverse()

        min_value = min(temp_items)

        for item in temp_items:
            self.push(item)
            if item == min_value:
                self.push(0)
