"""
Вычислите n-ое число Фибоначчи с использованием рекурсии и мемоизации.
"""


def fibonacci_memo(n: int, memo: Dict[int, int] = None) -> int:

    # Инициализация кэша при первом вызове
    if memo is None:
        memo = {0: 0, 1: 1}

    # Рекурсивное вычисление и запись в кэш
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
