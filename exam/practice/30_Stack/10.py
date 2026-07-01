'''
Создайте стек, который хранит элементы только определенной
длины (задается при инициализации).
'''


class Stack:
    def __init__(self, required_len: int):
        self.__items = []
        self.required_len = required_len

    def push(self, item):
        if hasattr(item, "__len__") and len(item) == self.required_len:
            self.__items.append(item)
        else:
            print(f"Элемент {item} отклонен: требуется длина {self.required_len}")

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
