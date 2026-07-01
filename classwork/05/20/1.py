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

    def remove_between(self, a, b):
        temp = []
        found = False

        while not self.is_empty():
            val = self.pop()
            if val in (a, b):
                found = True
                break
            temp.append(val)


        if not found:
            while temp: self.push(temp.pop())
            return

        while not self.is_empty():
            val = self.pop()
            if val in (a, b):
                break

        while temp:
            self.push(temp.pop())