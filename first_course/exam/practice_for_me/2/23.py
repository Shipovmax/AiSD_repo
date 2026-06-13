"""
Реализуйте параметризованный декоратор dec(a, b).

Декоратор должен анализировать результат математической функции:

если возвращаемая сумма положительна, он увеличивает итоговый результат на величину a,
а если отрицательна — уменьшает на величину b.
"""


def dec(a, b):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > 0:
                return result + a
            elif result < 0:
                return result - b
            return result

        return wrapper

    return decorator


@dec(a=10, b=5)
def calc_sum(x, y):
    return x + y
