"""
Реализуйте структуру данных однонаправленного связного списка
и напишите функцию добавления нового элемента в начало (слева) списка.
"""


class Node:
    def __init__(self, value, link=None):
        self.value = value
        self.link = link


class SingleLinkList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value, link=self.head)

        self.head = new_node

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.link
        print(" -> ".join(elements) + " -> None")
