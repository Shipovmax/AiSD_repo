"""
Реализуйте класс Стек.

Напишите функцию проверки содержимого: она должна определить,

является ли последовательность элементов в стеке строго упорядоченной
по возрастанию (от нижнего элементак верхнему).

Удалите из стека все элементы, которые не являются квадратами целых чисел.
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


def check_and_filter_stack(stack: Stack) -> bool:
    temp_stack = Stack()
    is_ordered = True

    if not stack.is_empty():
        current = stack.pop()
        temp_stack.push(current)

        while not stack.is_empty():
            prev = stack.pop()
            if prev >= current:
                is_ordered = False
            current = prev
            temp_stack.push(prev)

    while not temp_stack.is_empty():
        item = temp_stack.pop()

        if isinstance(item, (int, float)) and item >= 0:
            root = int(item**0.5)
            if root * root == item:
                stack.push(item)

    return is_ordered
