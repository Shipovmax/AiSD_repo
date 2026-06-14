"""
Реализуйте метод добавления нового узла в конец (справа)
однонаправленного связного списка,
корректно обрабатывая случай, когда список изначально пуст.
"""


class Node:
    def __init__(self, value, link=None):
        self.value = value
        self.link = link


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.link is not None:
            current = current.link

        current.link = new_node
