'''
Создайте декоратор dec(a, b).
Если сумма положительна, увеличивает результат на a, если отрицательна — уменьшает на b.
'''


def dec(a: int, b: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if result > 0:
                return result + a
            elif result < 0:
                return result - b
            else:
                return result

        return wrapper

    return decorator


@dec(a=2, b=10)
def calc_sum_positive(x, y):
    return x + y


@dec(a=2, b=10)
def calc_sum_negative(x, y):
    return x + y


print("=== ТЕСТ 1 (Положительный результат) ===")
print(f"Итог: {calc_sum_positive(5, 5)}")

print("\n=== ТЕСТ 2 (Отрицательный результат) ===")
print(f"Итог: {calc_sum_negative(-5, -2)}")
