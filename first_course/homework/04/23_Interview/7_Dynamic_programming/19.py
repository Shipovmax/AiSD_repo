"""
Числа Фибоначчи с мемоизацией
"""

from functools import lru_cache


# Рекурсия с мемоизацией
@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


# Итеративно — O(n) время, O(1) память
def fib_dp(n: int) -> int:
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


print(fib_dp(10))  # 55
