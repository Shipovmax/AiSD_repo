"""
Создайте специализированный класс Стек,

принимающий при инициализации кастомное правило фильтрации
(например, лямбда-функцию или ограничение на длину строк).

Стек должен принимать элементы через метод push() только в том случае,
если они удовлетворяют заданному правилу.

Дополнительно реализуйте метод, который считывает три нижних элемента структуры
и меняет местами верхний и нижний из этой тройки.
"""


class CustomFilterStack:
    def __init__(self, filter_func):
        self.items = []
        self.filter_func = filter_func

    def push(self, item):
        if self.filter_func(item):
            self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def swap_bottom_three(self):
        if self.size() < 3:
            return

        temp_stack = []
        while self.size() > 3:
            temp_stack.append(self.pop())

        third = self.pop()
        second = self.pop()
        first = self.pop()

        self.push(third)
        self.push(second)
        self.push(first)

        while temp_stack:
            self.push(temp_stack.pop())

    def __str__(self):
        return str(self.items)
