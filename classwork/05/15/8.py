"""
Найти минимальный элемент и вставить после него «0».
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

    def insert_zero_after_min(self):
        if self.is_empty():
            return

        min_val = min(self.sp)
        min_index = self.sp.index(min_val)

        self.sp.insert(min_index + 1, 0)


stack = Stack()
for x in [5, 2, 8, 1, 9]:
    stack.push(x)

stack.insert_zero_after_min()
print(stack.sp)
