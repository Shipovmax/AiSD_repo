"""
Найди индекс первого неповторяющегося символа в строке.
Если нет — верни -1.
"""

# Counter - Считает сколько есть каждого символа
from collections import Counter


def first_uniq_char(s: str) -> int:
    count = Counter(s)

    for i, c in enumerate(s):
        if count[c] == 1:
            return i

    return -1


# Тест
print(first_uniq_char("leetcode"))  # 0
print(first_uniq_char("loveleet"))  # 2
print(first_uniq_char("aabb"))  # -1
