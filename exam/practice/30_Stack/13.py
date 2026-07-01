'''
Сформируйте стек из строк.
Прочитайте три нижних элемента и поменяйте местами верхний и нижний.
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

    def swap_top_and_bottom_of_three(self):
        if self.size() < 3:
            print("В стеке меньше 3 элементов!")
            return

        temp_items = []
        while not self.is_empty():
            temp_items.append(self.pop())

        temp_items.reverse()

        bottom_three = temp_items[:3]

        print(f"Три нижних элемента: {bottom_three}")

        bottom_three[0], bottom_three[-1] = bottom_three[-1], bottom_three[0]

        temp_items[:3] = bottom_three

        for item in temp_items:
            self.push(item)


stack = Stack()
for s in ["первый", "второй", "третий", "четвертый", "пятый"]:
    stack.push(s)

print(f"Исходный стек: {stack.get_all_items()}")

stack.swap_top_and_bottom_of_three()

print(f"Итоговый стек:  {stack.get_all_items()}")
