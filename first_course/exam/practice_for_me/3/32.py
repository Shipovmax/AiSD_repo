"""
Реализуйте класс Стек.

Напишите функцию, которая принимает объект стека и
удаляет из него каждый второй элемент (начиная сверху).
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


def remove_every_second(stack: Stack):
    temp_stack = Stack()
    is_even = False

    while not stack.is_empty():
        item = stack.pop()
        if not is_even:
            temp_stack.push(item)
        is_even = not is_even

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
