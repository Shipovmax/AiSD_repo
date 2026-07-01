"""
Дан список целых чисел.

С помощью `map`/`filter`/`reduce` найдите произведение остатков от деления на 17, если остаток < 7.
"""

from functools import reduce


def process_numbers(numbers):

    remainders = map(lambda x: x % 17, numbers)

    valid_remainders = list(filter(lambda x: x < 7, remainders))
    if not valid_remainders:
        return 0

    return reduce(lambda x, y: x * y, valid_remainders)
