"""
Реализуйте класс Стек.

Напишите алгоритм, который вычисляет
среднее арифметическое всех числовых элементов в стеке,

а затем подсчитывает точное количество элементов,
значения которых строго больше этого среднего значения.
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


def analyze_stack(stack: Stack):
    temp_stack = Stack()
    total_sum = 0
    count = 0

    while not stack.is_empty():
        item = stack.pop()
        if isinstance(item, (int, float)):
            total_sum += item
            count += 1
        temp_stack.push(item)

    if count == 0:
        return 0, 0

    average = total_sum / count
    greater_than_avg_count = 0

    while not temp_stack.is_empty():
        item = temp_stack.pop()
        if isinstance(item, (int, float)) and item > average:
            greater_than_avg_count += 1
        stack.push(item)

    return average, greater_than_avg_count
