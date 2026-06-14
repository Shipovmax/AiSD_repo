"""
Напишите функцию для однонаправленного связного списка,

которая осуществляет поиск минимального значения среди всех узлов,
а также функцию подсчета суммы элементов, значения которых кратны 3.
"""


class Node:
    def __init__(self, value, link):
        self.value = value
        self.link = link


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value, link=self.head)

        self.head = new_node

    def get_min(self):
        if self.head is None:
            return None

        current = self.head
        min_value = current.value

        while current is not None:
            if current.value < min_value:
                min_value = current.value
            current = current.link

        return min_value

    def get_sum_divisible_by_3(self):
        total_sum = 0
        current = self.head

        while current is not None:
            if current.value % 3 == 0:
                total_sum += current.value
            current = current.link

        return total_sum
