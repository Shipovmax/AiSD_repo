"""
Дан список слов. Сгруппируй анаграммы вместе.
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(
        list
    )  # создал dict, где дефолтное значение для любого нового ключа — пустой список []

    for word in strs:
        """
        Разбиваю строку на кортеж (
        чтобы сделать ее ключом, тк список 
        нельзя использовать как ключ
        )
        Сортирую И эта последовательность будет 
        являться ключом для всех анаграмм 
        """

        key = tuple(sorted(word))
        groups[key].append((word))  # Добавляю в словарь key = ключ, word = значение

    return list(groups.values())  # Возвращает все группы анаграмм в виде списка


# Тесты
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["eat","tea","ate"],["tan","nat"],["bat"]]
