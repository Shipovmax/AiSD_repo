"""
Дан список слов.

С помощью `map`/`filter`/`reduce` найдите произведение остатков от деления длины слов на 7, если остаток > 4.
"""

from functools import reduce


def process_words(word_list):

    remainders = map(lambda word: len(word) % 7, word_list)

    valid_remainders = list(filter(lambda x: x > 4, remainders))
    if not valid_remainders:
        return 0

    product = reduce(lambda x, y: x * y, valid_remainders)

    return product
