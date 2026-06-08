'''
Создайте функцию three_args() (1, 2 или 3 строго ключевых параметра).
Декоратор должен выводить 0, если хотя бы один из параметров равен None.
'''


def check_none(func):
    def wrapper(*args, **kwargs):
        if None in kwargs.values():
            return 0
        return func(*args, **kwargs)

    return wrapper


@check_none
def three_args(*, first, second=None, third=None):
    return f"Все ок! Переданы: first={first}, second={second}, third={third}"


print(three_args(first=1, second=2, third=3))

print(three_args(first=1, second=2))

print(three_args(first=1, second=None, third=3))

print(three_args(1, 2, 3))  # TypeError: three_args() takes 0 positional arguments...
