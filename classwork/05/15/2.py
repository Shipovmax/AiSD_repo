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
    if stack.is_empty():
        stack.push(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(temp)


def reverse_stack(stack):
    if not stack.is_empty():
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)


my_stack = Stack()
my_stack.push("Книга 1")
my_stack.push("Книга 2")
my_stack.push("Книга 3")

print(f"До переворота (верхний): {my_stack.top()}") 

reverse_stack(my_stack)

print(f"После переворота (верхний): {my_stack.top()}") 

print("\nСодержимое стека снизу вверх:")
while not my_stack.is_empty():
    print(my_stack.pop())
