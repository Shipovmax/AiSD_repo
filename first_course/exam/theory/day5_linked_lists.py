"""
День 5: Линейные структуры данных с нуля.
Фокус: Узлы, Двусвязные списки, Кольцевые двусвязные списки и реверс "на месте" (in-place).
"""

from typing import Any, Optional, Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    """
    Generic-узел для двусвязного списка.
    Хранит данные и ссылки на предыдущий и следующий узлы.
    """
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional[Node[T]] = None
        self.prev: Optional[Node[T]] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

# -----------------------------------------------------------------------------
# Задача 1: Двусвязный список (Doubly Linked List - DLL)
# В отличие от односвязного, DLL позволяет обходить список в обе стороны.
# -----------------------------------------------------------------------------

class DoublyLinkedList(Generic[T]):
    """
    Полная реализация двусвязного списка без использования встроенных list.
    """
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self._size = 0

    def append(self, data: T) -> None:
        """
        Добавление элемента в конец списка.

        Логика:
        1. Создаем новый узел.
        2. Если список пуст, новый узел становится и началом, и концом.
        3. Если список не пуст, привязываем текущий хвост (tail) к новому узлу,
           а новому узлу проставляем ссылку назад на хвост.
        4. Обновляем хвост списка.

        Сложность:
        - Временная: O(1)
        - Пространственная: O(1)
        """
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            if self.tail:
                self.tail.next = new_node
                new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def prepend(self, data: T) -> None:
        """
        Добавление элемента в начало списка.

        Логика:
        - Создаем узел, привязываем его next к текущей голове (head),
          а голову prev к новому узлу. Обновляем head.

        Сложность:
        - Временная: O(1)
        - Пространственная: O(1)
        """
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def pop_back(self) -> Optional[T]:
        """
        Удаление и возврат последнего элемента.

        Логика:
        1. Если хвоста нет — возвращаем None.
        2. Запоминаем данные хвоста.
        3. Сдвигаем хвост на один узел назад (tail = tail.prev).
        4. Если новый хвост существует, обнуляем его ссылку next.
        5. Если список стал пустым, обнуляем и голову.

        Сложность:
        - Временная: O(1)
        - Пространственная: O(1)
        """
        if not self.tail:
            return None

        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        self._size -= 1
        return data

    def reverse_in_place(self) -> None:
        """
        Реверс списка "на месте" путем перестановки указателей next и prev.
        Это критически важная задача для экзамена.

        Логика работы:
        1. Идем по списку от головы до конца.
        2. Для каждого узла меняем местами ссылки на следующего и предыдущего.
        3. В конце обновляем голову и хвост списка.

        Сложность:
        - Временная: O(n) — проходим по списку один раз.
        - Пространственная: O(1) — не создаем новых структур, меняем ссылки.
        """
        curr = self.head
        self.tail = self.head # Старая голова станет новым хвостом

        last_node = None
        while curr:
            # Меняем указатели местами
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp

            last_node = curr # Запоминаем последний обработанный узел
            curr = temp # Переходим к следующему (который сохранили в temp)

        self.head = last_node

    def to_list(self) -> list[T]:
        """ Вспомогательный метод для тестирования: конвертация DLL в Python list. O(n) """
        res = []
        curr = self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res

    def __len__(self) -> int:
        return self._size

# -----------------------------------------------------------------------------
# Задача 2: Кольцевой двусвязный список (Circular Doubly Linked List - CDLL)
# Особенность: хвост.next = голова, а голова.prev = хвост.
# -----------------------------------------------------------------------------

class CircularDoublyLinkedList(Generic[T]):
    """
    Реализация кольцевого двусвязного списка.
    """
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self._size = 0

    def append(self, data: T) -> None:
        """
        Добавление в конец с поддержанием кольцевой структуры.

        Логика:
        1. Создаем новый узел.
        2. Если список пуст, узел ссылается сам на себя (head, next, prev = node).
        3. Если не пуст:
           - Находим хвост через head.prev.
           - Привязываем старый хвост к новому узлу.
           - Новый узел ссылается вперед на голову и назад на старый хвост.
           - Обновляем ссылку головы.prev на новый узел.

        Сложность:
        - Временная: O(1)
        - Пространственная: O(1)
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self._size += 1

    def to_list(self) -> list[T]:
        """ Конвертация CDLL в Python list для тестирования. O(n) """
        if not self.head:
            return []
        res = []
        curr = self.head
        while True:
            res.append(curr.data)
            curr = curr.next
            if curr == self.head: # Закольцевали
                break
        return res

if __name__ == "__main__":
    print("--- День 5: Тесты Связных Списков ---")

    # Тест Двусвязного списка
    dll = DoublyLinkedList[int]()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    print(f"DLL оригинал: {dll.to_list()}") # [0, 1, 2, 3]
    assert dll.to_list() == [0, 1, 2, 3]

    dll.reverse_in_place()
    print(f"DLL после реверса: {dll.to_list()}") # [3, 2, 1, 0]
    assert dll.to_list() == [3, 2, 1, 0]

    # Тест Кольцевого списка
    cdll = CircularDoublyLinkedList[int]()
    cdll.append(10)
    cdll.append(20)
    cdll.append(30)
    print(f"CDLL: {cdll.to_list()}") # [10, 20, 30]
    assert cdll.to_list() == [10, 20, 30]

    # Проверка кольцевой структуры
    assert cdll.head.prev.next == cdll.head
    assert cdll.head.next.prev == cdll.head

    print("Все тесты пятого дня успешно пройдены!")
