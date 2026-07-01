'''
Реализуйте класс Стек.
Разверните каждый второй элемент в обратном порядке.
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

    def reverse_every_second_item(self):
        temp_items = []
        while not self.is_empty():
            temp_items.append(self.pop())

        temp_items.reverse()

        for i in range(len(temp_items)):
            item = temp_items[i]
            if i % 2 == 1:
                item_str = str(item)
                reversed_str = item_str[::-1]

                if isinstance(item, int):
                    temp_items[i] = int(reversed_str)
                elif isinstance(item, float):
                    temp_items[i] = float(reversed_str)
                else:
                    temp_items[i] = reversed_str

        for item in temp_items:
            self.push(item)
