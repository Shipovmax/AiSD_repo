"""
Дан массив целых чисел.

Рассчитайте остаток от деления на 7 для каждого числа и найдите произведение остатков >4.
"""


def ostatok(array):
    product = 1
    has_valid_remainder = (
        False  # Флаг, чтобы проверить, нашли ли мы хоть один остаток > 4
    )

    for x in array:
        remainder = x % 7

        if remainder > 4:
            product *= remainder
            has_valid_remainder = True

    # Если подходящих остатков не было, логично вернуть 0 (или 1, в зависимости от требований)
    return product if has_valid_remainder else 0
