"""
Задачи с лямбда-функциями:

а) Поиск степеней двойки.
б) Сортировка кортежей по сумме элементов.
в) Поиск строк, состоящих только из гласных.

"""

first = lambda numbers: list(filter(lambda x: x > 0 and (x & (x - 1)) == 0, numbers))

second = lambda tuples_list: sorted(tuples_list, key=lambda t: sum(t))

third = lambda words_list: list(
    filter(
        lambda s: len(s) > 0 and all(c.lower() in "аеёиоуыэюя" for c in s), words_list
    )
)
