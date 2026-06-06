"""
Стек с поддержкой минимума (Min Stack):

Так как вы решаете задачи из Яндекс Контеста,
это очень частый алгоритм.

Модифицируй свой StackList так,
чтобы помимо стандартных операций у него был
метод get_min(), который мгновенно (за время O(1))
возвращает минимальный элемент в стеке.
"""


class StackList:
    def __init__(self):
        self._items = []
        self._min_stack = []

    def push(self, item):
        self._items.append(item)

        if not self._min_stack or item <= self._min_stack[-1]:
            self._min_stack.append(item)
        else:
            self._min_stack.append(self._min_stack[-1])

    def pop(self):
        if self.is_empty():
            return None
        self._min_stack.pop()
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def get_min(self):
        """Возвращает минимум за O(1)"""
        if not self._min_stack:
            return None
        return self._min_stack[-1]
