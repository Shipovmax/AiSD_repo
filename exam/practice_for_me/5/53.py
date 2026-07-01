"""
Дан массив целых чисел.

Рассчитайте остаток от деления на 7 для каждого числа.
Напишите программу, которая находит
произведение всех вычисленных остатков,
которые строго больше 4.
"""


def multiply_remainders_greater_than_four(nums):
    product = 1
    has_valid_remainders = False

    for num in nums:
        remainder = num % 7

        if remainder > 4:
            product *= remainder
            has_valid_remainders = True

    return product if has_valid_remainders else 0
