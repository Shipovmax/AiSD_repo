"""
Дан массив целых чисел
(элементы генерируются в диапазоне от -30 до 30).

Напишите алгоритм проверки:
если в массиве присутствует
хотя бы один отрицательный элемент,
массив должен быть отсортирован по возрастанию.

Если отрицательных элементов нет — отсортируйте его по убыванию.
"""


def check_and_sort(nums):
    has_negative = False

    for num in nums:
        if num < 0:
            has_negative = True
            break

    if has_negative:
        nums.sort()
    else:
        nums.sort(reverse=True)

    return nums
