class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.nxt = None


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def appendR(self, elem):
        a = Node(elem)

        if self.head is None:
            self.head = a
            self.tail = a
        else:
            a.prev = self.tail
            self.tail.nxt = a
            self.tail = a

    def __str__(self) -> str:
        res = []
        current = self.head
        while current:
            res.append(str(current.data))
            current = current.nxt
        return " <-> ".join(res) + " -> None"


s = DoublyLinkedList()
s.appendR(5)
s.appendR(6)
s.appendR(7)

print(s)