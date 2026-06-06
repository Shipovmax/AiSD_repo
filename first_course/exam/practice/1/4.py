"""
Найти k-ый наименьший элемент в списке (k начинается с 0).
"""


def quick_search(arr: List[int], k: int) -> int:

    # Базовый случай: в массиве остался один элемент
    if len(arr) == 1:
        return arr[0]

    # Выбор опорного элемента (берем средний по индексу)
    pivot = arr[len(arr) // 2]

    # Разделение массива (Partitioning)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивный спуск в нужную часть
    if k < len(left):
        return quick_search(left, k)
    elif k < len(left) + len(mid):
        return pivot  # Элемент найден
    else:
        # Пересчитываем k, вычитая количество элементов в left и mid
        return quick_search(right, k - len(left) - len(mid))
