"""
Задачи с лямбда-функциями:

а) Среднее арифметическое списка.
б) Сортировка строк по последней букве.
в) Поиск простых чисел в списке.
"""

from functools import reduce

average = lambda lst: reduce(lambda x, y: x + y, lst) / len(lst) if lst else 0

sort_by_last_letter = lambda words: sorted(words, key=lambda s: s[-1] if s else "")

is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

find_primes = lambda lst: list(filter(is_prime, lst))
