"""
Удалить минимальный элемент.
"""


class Stack:
    def __init__(self) -> None:
        self.sp = []

    def push(self, elem):
        self.sp.append(elem)

    def pop(self):
        if not self.is_empty():
            return self.sp.pop()
        return None

    def is_empty(self):
        return len(self.sp) == 0

    def lenn(self):
        return len(self.sp)

    def top(self):
        if not self.is_empty():
            return self.sp[-1]
        return None

    def remove_min(self):
        if not self.is_empty():
            min_val = min(self.sp)
            self.sp.remove(min_val)


stack = Stack()
for x in [10, 5, 20, 3, 15]:
    stack.push(x)

stack.remove_min()
print(stack.sp)
