"""
Задачи с лямбда-функциями:

а) Поиск квадратов чисел в списке.
б) Сортировка кортежей по первому элементу.
в) Поиск строк, начинающихся и заканчивающихся на одну букву.
"""

first = lambda list_input: list(map(lambda x: x**2, list_input))

second = lambda tuples_list: sorted(tuples_list, key=lambda x: x[0])

third = lambda words_list: list(
    filter(lambda s: len(s) > 0 and s[0].lower() == s[-1].lower(), words_list)
)
