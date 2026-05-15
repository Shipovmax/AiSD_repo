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


def check_brackets(code_string):
    s = Stack()

    for char in code_string:
        if char == "(":
            s.push(char)
        elif char == ")":
            if s.is_empty():
                return False
            s.pop()

    return s.is_empty()
