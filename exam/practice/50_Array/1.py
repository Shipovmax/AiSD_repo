"""
Дан массив целых чисел (от -20 до 20). Если ∣∑отрицательных∣>∑положительных,
отсортируйте по возрастанию, иначе — по убыванию.
"""


def process_and_sort(array):
    # Находим сумму положительных и абсолютную сумму отрицательных чисел
    sum_positive = sum(x for x in array if x > 0)
    sum_negative_abs = abs(sum(x for x in array if x < 0))

    # Проверяем условие и сортируем массив на месте
    if sum_negative_abs > sum_positive:
        array.sort()  # По возрастанию
    else:
        array.sort(reverse=True)  # По убыванию

    return array
