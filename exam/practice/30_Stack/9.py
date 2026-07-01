'''
Создайте стек, который хранит элементы только при
условии выполнения определенного правила (задается при инициализации).
'''


class Stack:
    def __init__(self, rule=lambda x: True):
        self.__items = []
        self.rule = rule

    def push(self, item):
        if self.rule(item):
            self.__items.append(item)
        else:
            print(f"Элемент {item} не удовлетворяет правилу стека")

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
