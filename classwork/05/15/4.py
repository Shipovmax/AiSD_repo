"""
Развернуть стек ("дно" стека сделать вершиной, а вершину - "дном").
"""


class Stack:
    def __init__(self) -> None:
        self.sp = []

    def push(self, elem):
        self.sp.append(elem)

    def pop(self):
        if self.is_empty():
            return None
        return self.sp.pop()

    def is_empty(self):
        return len(self.sp) == 0

    def lenn(self):
        return len(self.sp)

    def top(self):
        if self.is_empty():
            return None
        return self.sp[-1]


def reverse_stack(stack: Stack):
    temp_list = []

    while not stack.is_empty():
        temp_list.append(stack.pop())

    for item in temp_list:
        stack.push(item)


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push("Книга 1")
    my_stack.push("Книга 2")
    my_stack.push("Книга 3")

    reverse_stack(my_stack)

    while not my_stack.is_empty():
        print(my_stack.pop())
