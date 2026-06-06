"""
Вставить символ «*»
в середину стека, если четное число элементов,
а если нечетное, то после среднего элемента.
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

    def insert_star_middle(self):
        n = len(self.sp)
        if n == 0:
            self.push("*")
            return

        if n % 2 == 0:
            index = n // 2
        else:
            index = n // 2 + 1

        self.sp.insert(index, "*")


stack = Stack()
for i in range(1, 5):
    stack.push(i)

stack.insert_star_middle()
print(stack.sp)
