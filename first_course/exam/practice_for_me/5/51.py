"""
Дан массив целых чисел.

Напишите программу,
которая находит в нем количество пар соседних элементов,
имеющих разные знаки (один положительный, другой отрицательный).
"""


def count_different_sign_pairs(nums):
    count = 0
    for i in range(len(nums) - 1):
        if (nums[i] > 0 and nums[i + 1] < 0) or (nums[i] < 0 and nums[i + 1] > 0):
            count += 1
    return count
