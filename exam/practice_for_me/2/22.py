"""
Создайте функцию three_args(a, b, c), принимающую строго три ключевых параметра.

Напишите декоратор, который перехватывает выполнение и выводит 0,
если хотя бы один из переданных параметров равен None, не вызывая саму функцию.
"""


def checker(fun):
    def wrapper(*args, **kwargs):
        if None in args or None in kwargs.values():
            return 0
        return fun(*args, **kwargs)

    return wrapper


@checker
def three_args(*, a, b, c):
    return a + b + c
