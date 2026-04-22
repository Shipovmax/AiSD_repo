'''
Реализуй сортировку слиянием.
'''

def merge_sort(arr: list[int]) -> list[int]:
    # Базовый случай — массив из 0 или 1 элемента уже отсортирован
    if len(arr) <= 1:
        return arr

    # Делим массив пополам
    mid   = len(arr) // 2
    left  = merge_sort(arr[:mid])   # рекурсивно сортируем левую часть
    right = merge_sort(arr[mid:])   # рекурсивно сортируем правую часть

    # Сливаем две отсортированные половины
    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0  # указатели на текущий элемент в left и right

    # Сравниваем элементы из обоих массивов и берём меньший
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем остаток — один из массивов закончился, второй ещё нет
    result.extend(left[i:])   # остаток левого (если right закончился)
    result.extend(right[j:])  # остаток правого (если left закончился)

    return result

# Тест
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))