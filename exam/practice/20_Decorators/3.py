'''
Создайте функцию summa(start, end).
Если start > end, декоратор должен вывести разность чисел вместо суммы.
'''


def swap_to_difference(func):
    def wrapper(start, end):
        if start > end:
            return start - end
        return func(start, end)

    return wrapper


@swap_to_difference
def summa(start, end):
    return sum(range(start, end + 1))


print(f"Результат для (1, 5): {summa(1, 5)}")

print(f"Результат для (10, 2): {summa(10, 2)}")
