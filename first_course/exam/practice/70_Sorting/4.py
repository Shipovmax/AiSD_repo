"""
Реализуйте сортировку списка чисел по возрастанию методом пузырька.
"""


def bubble_sort(numbers):
    """
    Сортировка списка чисел по возрастанию методом пузырька (in-place).

    :param numbers: список чисел (изменяется на месте)
    """
    n = len(numbers)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]

    print("До сортировки:", nums)
    bubble_sort(nums)
    print("После сортировки:", nums)
