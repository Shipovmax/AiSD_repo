"""
День 4: Функциональное программирование в Python.
Фокус: Замыкания (closures), параметрические и универсальные декораторы,
использование дескрипторов @property для управления состоянием.
"""

from typing import Callable, Any, TypeVar, Dict, Optional, cast
from functools import wraps
import time

T = TypeVar('T')

# -----------------------------------------------------------------------------
# Задача 1: Паттерн "Замыкание" (Closure)
# Замыкание — это внутренняя функция, которая "запоминает" переменные из
# области видимости внешней функции даже после того, как внешняя функция завершилась.
# -----------------------------------------------------------------------------

def create_power_function(exponent: int) -> Callable[[float], float]:
    """
    Создает функцию, которая возводит число в заданную степень.

    Логика:
    - Внешняя функция принимает 'exponent'.
    - Внутренняя функция 'power' использует этот 'exponent' при каждом вызове.
    - Возвращая 'power', мы создаем замыкание.

    Сложность:
    - Временная: O(1) на создание, O(1) на выполнение.
    - Пространственная: O(1).
    """
    def power(base: float) -> float:
        return base ** exponent
    return power

# -----------------------------------------------------------------------------
# Задача 2: Параметрический декоратор
# Обычный декоратор просто оборачивает функцию. Параметрический декоратор
# — это функция, которая возвращает декоратор, позволяя настраивать его поведение.
# -----------------------------------------------------------------------------

def repeat_execution(times: int = 1) -> Callable[[Callable], Callable]:
    """
    Декоратор, который заставляет функцию выполниться 'times' раз.

    Логика:
    1. Внешний слой принимает параметр 'times'.
    2. Средний слой принимает саму функцию 'func'.
    3. Внутренний слой ('wrapper') запускает цикл, выполняя 'func' указанное количество раз.
    4. Возвращает результат последнего выполнения.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# -----------------------------------------------------------------------------
# Задача 3: Универсальный декоратор (Профилирование)
# Пример декоратора, который работает с любыми функциями, независимо от их аргументов.
# -----------------------------------------------------------------------------

def profile_performance(func: Callable[..., T]) -> Callable[..., T]:
    """
    Универсальный декоратор для измерения времени выполнения функции.

    Логика:
    - Использует `time.perf_counter()` для максимальной точности.
    - Использует `*args` и `**kwargs`, чтобы быть совместимым с любой сигнатурой функции.
    - Обертка `wraps` сохраняет метаданные исходной функции (__name__, __doc__).

    Сложность:
    - Временная: O(1) накладные расходы.
    - Пространственная: O(1).
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Функция {func.__name__!r} выполнена за {end_time - start_time:.6f}с")
        return result
    return wrapper

# -----------------------------------------------------------------------------
# Задача 4: Управляемое состояние с помощью @property
# Использование дескрипторов свойств позволяет реализовать геттеры и сеттеры,
# обеспечивая инкапсуляцию и валидацию данных "на лету".
# -----------------------------------------------------------------------------

class AccountBalance:
    """
    Класс управления балансом счета с валидацией через свойства.
    """
    def __init__(self, initial_balance: float):
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        """Геттер: возвращает текущий баланс. Сложность: O(1)."""
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        """
        Сеттер: устанавливает баланс с проверкой на отрицательное значение.
        Позволяет предотвратить некорректное состояние объекта.
        Сложность: O(1).
        """
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value

    def deposit(self, amount: float) -> None:
        """
        Метод пополнения баланса.
        Сложность: O(1).
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount

if __name__ == "__main__":
    print("--- День 4: Тесты Функционального Программирования ---")

    # Тест замыкания
    square = create_power_function(2)
    cube = create_power_function(3)
    print(f"Замыкание: 2^2={square(2)}, 2^3={cube(2)}")
    assert square(2) == 4
    assert cube(2) == 8

    # Тест параметрического декоратора
    @repeat_execution(times=3)
    def greet():
        print("Привет!")
        return "Done"

    print("Выполнение repeat_execution(3)...")
    assert greet() == "Done"

    # Тест универсального профилировщика
    @profile_performance
    def slow_sum(n: int) -> int:
        return sum(range(n))

    print("Профилирование slow_sum...")
    assert slow_sum(10**6) == sum(range(10**6))

    # Тест @property
    acc = AccountBalance(100.0)
    acc.deposit(50.0)
    print(f"Баланс счета: {acc.balance}")
    assert acc.balance == 150.0

    try:
        acc.balance = -10.0
    except ValueError as e:
        print(f"Поймали ожидаемую ошибку: {e}")

    print("Все тесты четвертого дня успешно пройдены!")
