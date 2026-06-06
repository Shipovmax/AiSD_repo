'''
Создайте двусвязный список для хранения информации о покупках в интернетмагазине.

Каждый элемент списка должен содержать название товара, цену, количество и дату покупки.
'''

from datetime import date
from decimal import Decimal


class PurchaseNode:
    __slots__ = ('name', 'price', 'count', 'purchase_date', 'prev', 'next')

    def __init__(self, name: str, price: Decimal, count: int, purchase_date: date):
        self.name = name
        self.price = price
        self.count = count
        self.purchase_date = purchase_date
        self.prev = None
        self.next = None


class PurchaseDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, node: PurchaseNode) -> None:
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self._size += 1

    def find_by_name(self, name: str):
        curr = self.head
        while curr:
            if curr.name == name:
                return curr
            curr = curr.next
        return None

    def remove(self, name: str) -> bool:
        node = self.find_by_name(name)
        if node is None:
            return False

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = node.next = None
        self._size -= 1
        return True

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __len__(self):
        return self._size
