"""
Дан массив целых чисел (от -30 до 30).
Если есть отрицательные элементы, отсортируйте по возрастанию, иначе — по убыванию.
"""


def process_and_sort(array):

    has_negative = any(x < 0 for x in array)
    array.sort(reverse=not has_negative)

    return array
