"""
Реализуйте функцию поиска и удаления узла по заданному значению в однонаправленном связном
списке. Необходимо корректно перестроить ссылки соседних узлов, обработать случаи удаления головного (первого)
элемента, единственного элемента списка, а также ситуацию, когда элемент не найден.
"""


class Node:
    def __init__(self, value, link=None):
        self.value = value
        self.link = link


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value, link=self.head)
        self.head = new_node

    def delete_by_value(self, target_value):
        if self.head is None:
            return False

        if self.head.value == target_value:
            self.head = self.head.link
            return True

        current = self.head
        while current.link is not None:
            if current.link.value == target_value:
                current.link = current.link.link
                return True
            current = current.link

        return False

    def display(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.value))
            current = current.link
        print(" -> ".join(elements) + " -> None")
