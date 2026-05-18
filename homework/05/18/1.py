from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional["Node"] = None


class StackList:
    def __init__(self):
        self.head: Optional[Node] = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None

        current_node = self.head
        value = current_node.value
        self.head = current_node.next
        return value

    def is_empty(self):
        return self.head is None


def check_brackets(code_string):
    stack = StackList()
    for char in code_string:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
