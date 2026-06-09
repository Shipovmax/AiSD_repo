"""
Дан список целых чисел.

С помощью `map`/`filter`/`reduce` найдите произведение чисел и сумму значений < 0.
"""

from functools import reduce


def summ_and_um(list_int):
    list_first_filter = list(filter(lambda x: x < 0, list_int))

    if not list_first_filter:
        return 0, 0

    total_product = reduce(lambda x, y: x * y, list_first_filter)
    total_sum = sum(list_first_filter)

    return total_product, total_sum
