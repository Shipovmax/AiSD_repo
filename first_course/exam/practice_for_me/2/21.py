"""
Реализуйте декоратор, который проверяет возвращаемое функцией число:
если оно четное, то возводит его в квадрат, если нечетное — в куб.
"""


def check_number(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            raise TypeError("Функция должна возвращать число")

        if result % 2 == 0:
            return result**2
        else:
            return result**3

    return wrapper


@check_number
def get_number(x):
    return x
