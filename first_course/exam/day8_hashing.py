"""
День 8: Хеширование и разрешение коллизий.
Фокус: Хеш-таблицы с методом цепочек (Chaining) и открытой адресацией (Open Addressing).
Линейное и квадратичное пробирование, использование специальных токенов удаления.
"""

from typing import Any, Optional, List, Generic, TypeVar

T = TypeVar('T')

# -----------------------------------------------------------------------------
# Задача 1: Хеш-таблица с методом цепочек (Separate Chaining)
# Это самый простой способ разрешения коллизий: каждая ячейка таблицы (bucket)
# представляет собой список всех элементов, которые попали в этот хеш.
# -----------------------------------------------------------------------------

class ChainingHashTable(Generic[T]):
    """
    Реализация хеш-таблицы, использующей метод цепочек.
    """
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.size = 0
        # Создаем список списков (корзины)
        self.table: List[List[tuple[Any, T]]] = [[] for _ in range(capacity)]

    def _hash(self, key: Any) -> int:
        """Вычисляет индекс корзины для ключа. Сложность: O(1)."""
        return hash(key) % self.capacity

    def put(self, key: Any, value: T) -> None:
        """
        Вставка или обновление значения.

        Логика:
        1. Вычисляем индекс корзины.
        2. Проходим по списку в этой корзине.
        3. Если ключ найден — обновляем значение.
        4. Если ключ не найден — добавляем новую пару в конец списка.

        Сложность:
        - Временная: O(1) в среднем, O(N) если все элементы попали в одну корзину.
        - Пространственная: O(1) на одну вставку.
        """
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def get(self, key: Any) -> Optional[T]:
        """
        Поиск значения по ключу.
        Логика: вычисляем хеш $\to$ ищем ключ в соответствующем списке.
        Сложность: O(1) в среднем, O(N) в худшем.
        """
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def remove(self, key: Any) -> bool:
        """
        Удаление ключа. Возвращает True при успехе.
        Сложность: O(1) в среднем, O(N) в худшем.
        """
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

# -----------------------------------------------------------------------------
# Задача 2: Хеш-таблица с открытой адресацией (Open Addressing)
# Здесь нет списков внутри ячеек. Если ячейка занята, мы ищем следующую свободную
# по определенному правилу (пробирование).
# -----------------------------------------------------------------------------

class OpenAddressingHashTable(Generic[T]):
    """
    Реализация хеш-таблицы с открытой адресацией.
    Поддерживает режимы 'linear' (линейное) и 'quadratic' (квадратичное) пробирование.
    """
    # Специальный токен для удаленных элементов.
    # Важно: если мы просто поставим None, мы разорвем цепочку пробирования,
    # и поиск элементов, которые были вставлены ПОСЛЕ удаленного, перестанет работать.
    DELETED = object()

    def __init__(self, capacity: int = 10, mode: str = 'linear'):
        self.capacity = capacity
        self.mode = mode
        self.size = 0
        self.table: List[Optional[tuple[Any, T]]] = [None] * capacity

    def _hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    def _probe(self, key: Any, attempt: int) -> int:
        """
        Вычисляет индекс ячейки на i-й попытке пробирования.

        Логика:
        - Линейно: (hash + i) % capacity.
        - Квадратично: (hash + i^2) % capacity. Помогает избежать первичного кластерирования.
        """
        base = self._hash(key)
        if self.mode == 'linear':
            return (base + attempt) % self.capacity
        else: # quadratic
            return (base + attempt**2) % self.capacity

    def put(self, key: Any, value: T) -> None:
        """
        Вставка значения с использованием пробирования.

        Логика:
        1. Пробуем найти свободную ячейку (None или DELETED).
        2. Если находим ячейку с тем же ключом — обновляем значение.
        3. Если прошли весь массив и не нашли места $\to$ Overflow.

        Сложность:
        - Временная: O(1) в среднем, O(N) при высокой заполненности.
        """
        attempt = 0
        while attempt < self.capacity:
            idx = self._probe(key, attempt)
            slot = self.table[idx]
            if slot is None or slot is self.DELETED:
                self.table[idx] = (key, value)
                self.size += 1
                return
            if slot[0] == key:
                self.table[idx] = (key, value)
                return
            attempt += 1
        raise Exception("Hash Table Overflow")

    def get(self, key: Any) -> Optional[T]:
        """
        Поиск значения.
        Важно: поиск продолжается, если мы встретили DELETED, и останавливается только на None.
        Сложность: O(1) в среднем, O(N) в худшем.
        """
        attempt = 0
        while attempt < self.capacity:
            idx = self._probe(key, attempt)
            slot = self.table[idx]
            if slot is None:
                return None # Ключ точно не в таблице
            if slot is not self.DELETED and slot[0] == key:
                return slot[1]
            attempt += 1
        return None

    def remove(self, key: Any) -> bool:
        """
        Удаление ключа путем пометки ячейки как DELETED.
        Сложность: O(1) в среднем, O(N) в худшем.
        """
        attempt = 0
        while attempt < self.capacity:
            idx = self._probe(key, attempt)
            slot = self.table[idx]
            if slot is None:
                return False
            if slot is not self.DELETED and slot[0] == key:
                self.table[idx] = self.DELETED
                self.size -= 1
                return True
            attempt += 1
        return False

if __name__ == "__main__":
    print("--- День 8: Тесты Хеширования ---")

    # Тест метода цепочек
    ct = ChainingHashTable[int](capacity=5)
    ct.put("a", 1)
    ct.put("b", 2)
    ct.put("f", 3) # Скорее всего будет коллизия с "a" при capacity=5
    print(f"Цепочки Get 'f': {ct.get('f')}")
    assert ct.get("f") == 3
    ct.remove("a")
    assert ct.get("a") is None

    # Тест открытой адресации (Линейной)
    oat_lin = OpenAddressingHashTable[int](capacity=10, mode='linear')
    oat_lin.put("k1", 100)
    oat_lin.put("k2", 200)
    oat_lin.remove("k1")
    # Проверяем, что поиск k2 всё еще работает после удаления k1
    oat_lin.put("k3", 300)
    print(f"Открытая адресация Get 'k2': {oat_lin.get('k2')}")
    assert oat_lin.get("k2") == 200

    # Тест открытой адресации (Квадратичной)
    oat_quad = OpenAddressingHashTable[int](capacity=10, mode='quadratic')
    oat_quad.put("x", 10)
    oat_quad.put("y", 20)
    assert oat_quad.get("x") == 10

    print("Все тесты восьмого дня успешно пройдены!")
