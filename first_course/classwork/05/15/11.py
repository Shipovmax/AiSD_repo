class BoundedStack:
    def __init__(self, max_limit):
        self._data = []
        self._max_limit = max_limit

    def push(self, e):
        if len(self._data) >= self._max_limit:
            raise OverflowError("Stack Overflow")
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)
