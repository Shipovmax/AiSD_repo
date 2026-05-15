'''
Удалить элемент, 
который находится в середине сте-ка, 
если нечетное число элементов, 
а если четное, то два сред-них.
'''

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

def delete_middle(stack: Stack):
    n = stack.lenn()
    if n == 0:
        return

    temp_stack = []
    
    mid_index = n // 2
    if n % 2 == 0:
        to_pop = n - mid_index + 1
        to_remove = 2
    else:
        to_pop = n - mid_index
        to_remove = 1

    for _ in range(to_pop - to_remove):
        temp_stack.append(stack.pop())

    for _ in range(to_remove):
        stack.pop()

    while temp_stack:
        stack.push(temp_stack.pop())

if __name__ == "__main__":
    s = Stack()
    for i in range(1, 6):
        s.push(i)
    
    delete_middle(s)
    
    while not s.is_empty():
        print(s.pop())