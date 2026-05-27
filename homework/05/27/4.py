def merge_sort(arr):
    # Базовый случай: если в массиве 1 элемент или меньше, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Рекурсивно сортируем левую часть
    right_half = merge_sort(arr[mid:])  # Рекурсивно сортируем правую часть

    # Сливаем две отсортированные половины в одну
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # Пока в обеих половинах есть элементы, выбираем меньший и добавляем в результат
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Если в одной из половин остались элементы (одна закончилась быстрее),
    # просто дописываем их в конец результата
    result.extend(left[i:])
    result.extend(right[j:])

    return result
