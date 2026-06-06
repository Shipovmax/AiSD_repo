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


def remove_every_second(stack: Stack):
    temp_stack = Stack()
    index = 1

    while not stack.is_empty():
        item = stack.pop()
        if item != 5 :
            temp_stack.push(item)
        index += 1

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())


if __name__ == "__main__":
    my_stack = Stack()
    for i in range(1, 7):
        my_stack.push(i)

    remove_every_second(my_stack)

    while not my_stack.is_empty():
        print(my_stack.pop())
