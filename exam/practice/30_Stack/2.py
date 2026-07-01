'''
Реализуйте класс Стек.
Проверьте, является ли содержимое упорядоченным по возрастанию.
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

    def is_sorted_ascending(self) -> bool:
        if self.size() <= 1:
            return True

        items = self.get_all_items()
        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                return False
        return True
