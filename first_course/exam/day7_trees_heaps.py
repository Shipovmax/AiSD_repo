"""
День 7: Двоичные деревья поиска и Кучи.
Фокус: BST с полной реализацией удаления (все 3 случая), обходы дерева,
реализация MinHeap через массив с операциями Sift-up и Sift-down.
"""

from typing import Optional, List, Generic, TypeVar

T = TypeVar('T')

# -----------------------------------------------------------------------------
# Задача 1: Двоичное дерево поиска (Binary Search Tree - BST)
# BST гарантирует, что для любого узла: левый потомок < узел < правый потомок.
# -----------------------------------------------------------------------------

class BSTNode(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.left: Optional[BSTNode[T]] = None
        self.right: Optional[BSTNode[T]] = None

class BinarySearchTree(Generic[T]):
    """
    Реализация BST с детальной логикой удаления узлов.
    """
    def __init__(self):
        self.root: Optional[BSTNode[T]] = None

    def insert(self, value: T) -> None:
        """
        Вставка значения в дерево.
        Логика: спускаемся по дереву, пока не найдем свободное место (None),
        согласно правилу: меньше $\to$ налево, больше $\to$ направо.

        Сложность: O(log N) в среднем, O(N) если дерево выродилось в список.
        """
        if not self.root:
            self.root = BSTNode(value)
            return

        curr = self.root
        while True:
            if value < curr.value:
                if not curr.left:
                    curr.left = BSTNode(value)
                    break
                curr = curr.left
            elif value > curr.value:
                if not curr.right:
                    curr.right = BSTNode(value)
                    break
                curr = curr.right
            else:
                break # Значение уже существует

    def remove(self, value: T) -> None:
        """
        Удаление узла из BST. Самая сложная часть работы с деревьями.
        """
        self.root = self._remove_recursive(self.root, value)

    def _remove_recursive(self, node: Optional[BSTNode[T]], value: T) -> Optional[BSTNode[T]]:
        """
        Рекурсивный метод удаления. Обрабатывает 3 академических случая.

        Логика:
        1. Сначала находим узел, который нужно удалить.
        2. Случай 1: Узел — лист (нет детей). Просто удаляем его (возвращаем None).
        3. Случай 2: У узла один ребенок. Заменяем узел его ребенком.
        4. Случай 3: У узла два ребенка.
           - Находим "преемника" (Succeedor) — это самый левый узел в правом поддереве.
           - Копируем значение преемника в текущий узел.
           - Рекурсивно удаляем преемника из правого поддерева (он гарантированно попадет в случай 1 или 2).

        Сложность: O(log N) в среднем, O(N) в худшем.
        """
        if not node:
            return None

        if value < node.value:
            node.left = self._remove_recursive(node.left, value)
        elif value > node.value:
            node.right = self._remove_recursive(node.right, value)
        else:
            # Нашли узел для удаления
            # Случай 1 и 2: нет левого или правого ребенка
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Случай 3: два ребенка
            successor = self._get_min(node.right)
            node.value = successor.value
            node.right = self._remove_recursive(node.right, successor.value)

        return node

    def _get_min(self, node: BSTNode[T]) -> BSTNode[T]:
        """Находит самый левый узел (минимум) в поддереве."""
        curr = node
        while curr.left:
            curr = curr.left
        return curr

    def inorder(self, node: Optional[BSTNode[T]], res: List[T]) -> None:
        """
        Центрированный обход (In-order traversal): Лево $\to$ Корень $\to$ Право.
        Результатом обхода BST всегда является отсортированный список.
        Сложность: O(N) время, O(N) память.
        """
        if node:
            self.inorder(node.left, res)
            res.append(node.value)
            self.inorder(node.right, res)

# -----------------------------------------------------------------------------
# Задача 2: Бинарная Куча (MinHeap)
# Куча — это почти полное бинарное дерево, где родитель всегда меньше своих детей.
# Хранится в массиве: для узла i, дети находятся в 2i+1 и 2i+2.
# -----------------------------------------------------------------------------

class MinHeap(Generic[T]):
    """
    Реализация Min-Heap для приоритетных очередей.
    """
    def __init__(self):
        self.heap: List[T] = []

    def push(self, value: T) -> None:
        """
        Добавление элемента.
        Логика:
        1. Добавляем элемент в самый конец массива (поддерживаем полноту дерева).
        2. Выполняем операцию "просеивания вверх" (Sift-up), чтобы восстановить
           свойство кучи (родитель < ребенок).

        Сложность: O(log N) — высота дерева.
        """
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> Optional[T]:
        """
        Извлечение минимального элемента (корня).
        Логика:
        1. Корень кучи — всегда минимальный элемент.
        2. Заменяем корень последним элементом массива.
        3. Выполняем "просеивание вниз" (Sift-down), чтобы восстановить свойство кучи.

        Сложность: O(log N) — высота дерева.
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_val

    def _sift_up(self, idx: int) -> None:
        """Восстановление свойства кучи при движении вверх."""
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._sift_up(parent)

    def _sift_down(self, idx: int) -> None:
        """Восстановление свойства кучи при движении вниз."""
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._sift_down(smallest)

if __name__ == "__main__":
    print("--- День 7: Тесты Деревьев и Куч ---")

    # Тест BST
    bst = BinarySearchTree[int]()
    for x in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(x)

    res = []
    bst.inorder(bst.root, res)
    print(f"BST Inorder (отсортировано): {res}")
    assert res == sorted([50, 30, 70, 20, 40, 60, 80])

    # Тест удаления BST
    bst.remove(20) # Случай 1/2
    bst.remove(30) # Случай 3 (два ребенка)
    res = []
    bst.inorder(bst.root, res)
    print(f"BST Inorder после удаления 20 и 30: {res}")
    assert res == sorted([50, 70, 40, 60, 80])

    # Тест MinHeap
    heap = MinHeap[int]()
    for x in [10, 5, 20, 1, 15]:
        heap.push(x)

    results = []
    while True:
        val = heap.pop()
        if val is None: break
        results.append(val)

    print(f"Последовательность извлечения из кучи: {results}")
    assert results == [1, 5, 10, 15, 20]

    print("Все тесты седьмого дня успешно пройдены!")
