"""
Найти максимальный элемент и вставить после него «0».
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

    def insert_zero_after_max(self):
        if self.is_empty():
            return

        max_val = max(self.sp)
        max_index = self.sp.index(max_val)

        self.sp.insert(max_index + 1, 0)


stack = Stack()
for x in [5, 2, 8, 1, 9]:
    stack.push(x)

stack.insert_zero_after_max()
print(stack.sp)
