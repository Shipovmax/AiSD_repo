"""
Реализовать декоратор с именем not_none, который генерирует
исключительную ситуацию если декорируемая функция вернула значения None.
"""


def not_none(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result is None:
            raise AttributeError("Function returned None")

        return result

    return wrapper


@not_none
def add(a, b):
    c = a + b
    return None


try:
    add(1, 2)
except AttributeError:
    print("AttributeError")
