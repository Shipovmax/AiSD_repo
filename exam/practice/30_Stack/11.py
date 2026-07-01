'''
Создайте стек для строк, отсортированных по алфавиту.
При получении элементов они должны быть отсортированы.
'''


class AlphabeticalStack:
    def __init__(self):
        self.__items = []

    def push(self, item: str):
        if not isinstance(item, str):
            print(f"Элемент {item} отклонен: стек принимает только строки")
            return

        temp_items = []
        while not self.is_empty() and self.peek() < item:
            temp_items.append(self.pop())

        self.__items.append(item)

        while temp_items:
            self.__items.append(temp_items.pop())

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
