'''
Реализовать класс бинарного дерева.
Написать функцию для поиска элемента в бинарном дереве.
'''


class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)


def search(node, key):
    if node is None or node.val == key:
        return node

    if key < node.val:
        return search(node.left, key)

    return search(node.right, key)


tree = BinaryTree()
elements = [50, 30, 20, 40, 70, 60, 80]

for el in elements:
    tree.insert(el)

search_keys = [40, 90]

for key in search_keys:
    result = search(tree.root, key)
    if result:
        print(f"Элемент {key} найден в дереве.")
    else:
        print(f"Элемент {key} НЕ найден в дереве.")