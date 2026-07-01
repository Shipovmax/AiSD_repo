"""
Реализуйте класс Стек на базе стандартного списка (list).

Напишите метод, который меняет местами
самый первый (нижний) и самый последний (верхний) элементы в стеке,
не разрушая промежуточную структуру.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Реверс пустого стека невозможен")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def swap_ends(self):
        if self.size() < 2:
            return

        top = self.pop()

        temp_stack = Stack()
        while self.size() > 1:
            temp_stack.push(self.pop())

        bottom = self.pop()

        self.push(top)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        self.push(bottom)

    def __str__(self):
        return str(self.items)
