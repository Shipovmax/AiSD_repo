"""
Задачи с лямбда-функциями:

а) Поиск чисел > среднего арифметического.
б) Сортировка строк по длине.
в) Поиск кубов чисел в списке.
"""

first = lambda lst: list(filter(lambda x: x > sum(lst) / len(lst), lst))

second = lambda lst: sorted(lst, key=lambda s: len(s))

third = lambda lst: list(map(lambda x: x**3, lst))
