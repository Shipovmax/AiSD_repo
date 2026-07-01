"""
Дан массив целых чисел (от 0 до 100).

Если количество четных элементов на нечетных местах больше количества нечетных
на четных, отсортируйте по возрастанию, иначе по убыванию.
"""


def process_and_sort(array):
    even_on_odd_slots = 0  # Четные элементы на нечетных местах
    odd_on_even_slots = 0  # Нечетные элементы на четных местах

    for index in range(len(array)):
        element = array[index]

        # Если место (индекс) нечетное
        if index % 2 != 0:
            if element % 2 == 0:
                even_on_odd_slots += 1

        # Если место (индекс) четное
        else:
            if element % 2 != 0:
                odd_on_even_slots += 1

    # Проверяем условие для выбора направления сортировки
    if even_on_odd_slots > odd_on_even_slots:
        array.sort()  # По возрастанию
    else:
        array.sort(reverse=True)  # По убыванию

    return array
