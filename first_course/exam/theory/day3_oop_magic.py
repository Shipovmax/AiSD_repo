"""
День 3: Глубокое ООП и Магические Методы.
Фокус: Перегрузка операторов, создание функторов и реализация протокола итератора (__iter__, __next__).
"""

from typing import Any, Iterator, Optional, List, Generic, TypeVar

T = TypeVar('T')

# -----------------------------------------------------------------------------
# Задача 1: Класс Vector2D (Перегрузка операторов)
# Реализация двумерного вектора с полной поддержкой арифметических и логических операций.
# Это классический пример того, как сделать пользовательский класс "родным" для Python.
# -----------------------------------------------------------------------------

class Vector2D:
    """
    Реализация 2D вектора, демонстрирующая перегрузку магических методов.
    """

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float: return self._x

    @property
    def y(self) -> float: return self._y

    # --- Арифметические операторы ---
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        """
        Сложение векторов: (x1, y1) + (x2, y2) = (x1+x2, y1+y2).
        Сложность: O(1) время, O(1) память.
        """
        if not isinstance(other, Vector2D):
            return NotImplemented # Сообщаем Python, что данный тип не поддерживает сложение
        return Vector2D(self._x + other._x, self._y + other._y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        """
        Вычитание векторов: (x1, y1) - (x2, y2) = (x1-x2, y1-y2).
        Сложность: O(1) время, O(1) память.
        """
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self._x - other._x, self._y - other._y)

    def __mul__(self, scalar: float) -> 'Vector2D':
        """
        Умножение вектора на скаляр: (x, y) * s = (x*s, y*s).
        Сложность: O(1) время, O(1) память.
        """
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector2D(self._x * scalar, self._y * scalar)

    def __truediv__(self, scalar: float) -> 'Vector2D':
        """
        Деление вектора на скаляр: (x, y) / s = (x/s, y/s).
        Сложность: O(1) время, O(1) память.
        """
        if not isinstance(scalar, (int, float)) or scalar == 0:
            return NotImplemented
        return Vector2D(self._x / scalar, self._y / scalar)

    # --- Логические операторы ---
    def __eq__(self, other: Any) -> bool:
        """
        Сравнение на равенство. Два вектора равны, если их координаты совпадают.
        Сложность: O(1) время, O(1) память.
        """
        if not isinstance(other, Vector2D):
            return False
        return self._x == other._x and self._y == other._y

    def __lt__(self, other: 'Vector2D') -> bool:
        """
        Сравнение по длине (модулю). Длина вектора: sqrt(x^2 + y^2).
        Для оптимизации сравниваем квадраты длин, чтобы избежать дорогого sqrt().
        Сложность: O(1) время, O(1) память.
        """
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (self._x**2 + self._y**2) < (other._x**2 + other._y**2)

    # --- Строковое представление ---
    def __repr__(self) -> str:
        """Техническое представление объекта (для отладки)."""
        return f"Vector2D({self._x}, {self._y})"

    def __str__(self) -> str:
        """Красивое представление объекта для пользователя."""
        return f"({self._x}, {self._y})"

# -----------------------------------------------------------------------------
# Задача 2: Паттерн "Функтор" (Callable Class)
# Класс, который ведет себя как функция. Используется для сохранения состояния
# между вызовами без использования глобальных переменных.
# -----------------------------------------------------------------------------

class SequenceGenerator:
    """
    Функтор, который генерирует последовательность чисел.
    """
    def __init__(self, start: int = 0, step: int = 1):
        self.current = start
        self.step = step

    def __call__(self, count: int = 1) -> List[int]:
        """
        Позволяет вызвать объект класса как функцию: gen(3).
        Возвращает список из следующих 'count' элементов последовательности.

        Сложность:
        - Временная: O(count)
        - Пространственная: O(count)
        """
        result = []
        for _ in range(count):
            result.append(self.current)
            self.current += self.step
        return result

# -----------------------------------------------------------------------------
# Задача 3: Кастомный протокол итератора (__iter__ и __next__)
# Реализация объекта, который можно обходить в цикле for.
# Это основа всех коллекций в Python.
# -----------------------------------------------------------------------------

class CustomRange:
    """
    Реализация range-подобного объекта через протокол итерации.
    """
    def __init__(self, start: int, stop: int, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self._current = start # Внутренний указатель состояния

    def __iter__(self) -> Iterator[int]:
        """
        Возвращает сам объект итератора.
        В данном случае объект CustomRange сам является итератором.
        Сложность: O(1).
        """
        return self

    def __next__(self) -> int:
        """
        Возвращает следующее значение или выбрасывает StopIteration.

        Логика:
        1. Проверяем, не вышли ли мы за границу stop (учитывая знак step).
        2. Если вышли — сигнализируем циклу for о завершении через StopIteration.
        3. Если нет — запоминаем текущее значение, сдвигаем указатель и возвращаем результат.

        Сложность: O(1).
        """
        # Проверка условия завершения для положительного и отрицательного шага
        if (self.step > 0 and self._current >= self.stop) or \
           (self.step < 0 and self._current <= self.stop):
            raise StopIteration

        val = self._current
        self._current += self.step
        return val

if __name__ == "__main__":
    print("--- День 3: Тесты ООП и Магических Методов ---")

    # Тест Vector2D
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)
    v3 = v1 + v2
    print(f"Сложение векторов: {v1} + {v2} = {v3}")
    assert v3 == Vector2D(4, 6)

    v4 = v1 * 2.0
    print(f"Умножение на скаляр: {v1} * 2 = {v4}")
    assert v4 == Vector2D(2, 4)

    print(f"Сравнение по длине: {v1} < {v2} это {v1 < v2}")
    assert v1 < v2

    # Тест Функтора
    gen = SequenceGenerator(start=10, step=5)
    print(f"Последовательность функтора: {gen(3)}") # [10, 15, 20]
    assert gen(2) == [25, 30]

    # Тест Итератора
    my_range = CustomRange(0, 10, 2)
    res = [x for x in my_range]
    print(f"Результат CustomRange: {res}")
    assert res == [0, 2, 4, 6, 8]

    print("Все тесты третьего дня успешно пройдены!")
