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


my_stack = Stack()

my_stack.push("Книга 1")
my_stack.push("Книга 2")

print(f"Верхний элемент: {my_stack.top()}")
print(f"Пустой ли стек? {my_stack.is_empty()}")
