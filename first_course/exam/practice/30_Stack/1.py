'''
Реализуйте класс Стек.
Найдите количество элементов, которые больше среднего значения всех элементов стека.
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

    def count_above_average(self) -> int:
        if self.is_empty():
            return 0

        items = self.get_all_items()
        average = sum(items) / len(items)

        count = sum(1 for x in items if x > average)
        return count


stack = Stack()
for value in [10, 20, 30, 40, 50]:
    stack.push(value)

print(f"Элементы стека: {stack.get_all_items()}")
print(f"Количество элементов больше среднего значения: {stack.count_above_average()}")
