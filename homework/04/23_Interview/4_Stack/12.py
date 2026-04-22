'''
Реализуй стек с операциями push, pop, top и getMin за O(1).
'''

class MinStack:
    def __init__(self):
        self.min_stack = []
        self.stack     = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.min_stack:
            self.min_stack.append(min(val,self.min_stack[-1]))