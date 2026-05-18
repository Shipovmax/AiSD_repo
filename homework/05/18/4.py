"""
Постфиксная запись (Обратная польская запись):

Напиши функцию, которая вычисляет математическое выражение,
записанное в постфиксной форме, используя стек.

Например, на вход подается список ["2", "3", "+", "5", "*"]
(что означает (2 + 3) * 5),
и функция должна вернуть 25.
"""


class stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        """Добавляет элемент в конец (на вершину стека)."""
        self._items.append(item)

    def pop(self):
        """Удаляет и возвращает верхний элемент. Обрабатывает пустой стек."""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        """Возвращает верхний элемент без удаления."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        """Возвращает True, если стек пуст."""
        return len(self._items) == 0


def evaluate_postfix(expression):
    stack = []

    # Словарь для быстрой обработки операций
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b),  # Целочисленное деление как в большинстве задач
    }

    for token in expression:
        if token in operations:
            # Важен порядок: b достаем первым (он был положен в стек последним)
            b = stack.pop()
            a = stack.pop()
            result = operations[token](a, b)
            stack.append(result)
        else:
            # Превращаем строку в число и кладем в стек
            stack.append(int(token))

    return stack[0]
