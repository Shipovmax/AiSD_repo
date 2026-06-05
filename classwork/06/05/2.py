'''
Реализовать класс бинарного дерева.
Написать функцию для проверки, является ли бинарное дерево сбалансированным.
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
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)


def get_height(node):
    if node is None:
        return 0
    left_h = get_height(node.left)
    right_h = get_height(node.right)
    return max(left_h, right_h) + 1


def is_balanced(node):
    if node is None:
        return True

    left_h = get_height(node.left)
    right_h = get_height(node.right)

    if abs(left_h - right_h) > 1:
        return False

    return is_balanced(node.left) and is_balanced(node.right)
