"""
Реализовать декоратор, который выводит на печать возвращаемые значения функции.
"""


def print_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Return:", result)
        return result

    return wrapper


@print_return
def add(a, b):
    return a + b


@print_return
def greet(name):
    return f"Hello {name}"


add(2, 3)
greet("Max")
