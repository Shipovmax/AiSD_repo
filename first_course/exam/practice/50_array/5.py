"""
Даны два массива. Создайте массив из общих элементов.
"""


def find_common_elements(array1, array2):
    # Превращаем массивы во множества и находим их пересечение
    common = set(array1).intersection(set(array2))

    # Возвращаем результат в виде обычного списка
    return list(common)
