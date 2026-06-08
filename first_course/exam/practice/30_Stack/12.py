'''
Создайте два стека и поменяйте их содержимое местами.
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

    def swap_contents(self, other_stack):
        if not isinstance(other_stack, Stack):
            raise TypeError("Объект должен быть экземпляром класса Stack")

        temp1 = []
        temp2 = []

        while not self.is_empty():
            temp1.append(self.pop())

        while not other_stack.is_empty():
            temp2.append(other_stack.pop())

        for item in reversed(temp2):
            self.push(item)

        for item in reversed(temp1):
            other_stack.push(item)


stack_A = Stack()
stack_B = Stack()

for val in [1, 2, 3]:
    stack_A.push(val)

for val in ["A", "B", "C"]:
    stack_B.push(val)

print(f"До обмена -> Стек А: {stack_A.get_all_items()}, Стек Б: {stack_B.get_all_items()}")

stack_A.swap_contents(stack_B)

print(f"После обмена -> Стек А: {stack_A.get_all_items()}, Стек Б: {stack_B.get_all_items()}")
