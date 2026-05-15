"""
Дан стек. Необходимо перевернуть его содержимое так,
чтобы верхний элемент стал нижним, а нижний — верхним.
"""


class Stack:
    def __init__(self) -> None:
        self.sp = []

    def push(self, elem):
        self.sp.append(elem)

    def pop(self):
        return self.sp.pop()

    def is_empty(self):
        return len(self.sp) == 0

    def lenn(self):
        return len(self.sp)

    def top(self):
        return self.sp[-1]


def insert_at_bottom(stack, item):
    """Вставляет элемент в самый низ стека с помощью рекурсии."""
    if stack.is_empty():
        stack.push(item)
    else:
        # Извлекаем текущий элемент, чтобы дойти до дна
        temp = stack.pop()
        insert_at_bottom(stack, item)
        # Кладем извлеченный элемент обратно сверху
        stack.push(temp)


def reverse_stack(stack):
    """Переворачивает стек, используя рекурсивные вызовы."""
    if not stack.is_empty():
        # Достаем верхний элемент
        temp = stack.pop()
        # Рекурсивно переворачиваем то, что осталось
        reverse_stack(stack)
        # Кладем первый извлеченный элемент в самый низ
        insert_at_bottom(stack, temp)


my_stack = Stack()
my_stack.push("Книга 1")
my_stack.push("Книга 2")
my_stack.push("Книга 3")

print(f"До переворота (верхний): {my_stack.top()}")  # Ожидаем Книга 3

reverse_stack(my_stack)

print(f"После переворота (верхний): {my_stack.top()}")  # Ожидаем Книга 1

print("\nСодержимое стека снизу вверх:")
while not my_stack.is_empty():
    print(my_stack.pop())
