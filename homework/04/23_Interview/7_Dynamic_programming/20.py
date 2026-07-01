"""
Лестница из n ступенек. За один шаг можно подняться на 1 или 2 ступеньки.
Сколько способов добраться до вершины?
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    prev, curr = 1, 2

    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr


# Тесты
print(climb_stairs(2))  # 2
print(climb_stairs(3))  # 3
print(climb_stairs(5))  # 8
