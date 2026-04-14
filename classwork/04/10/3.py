'''
Реализовать декоратор с именем print_type, выводящий
на печать тип значения, возвращаемого декорируемой функцией.
'''


def print_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Type:", type(result))
        return result

    return wrapper


@print_type
def add(a, b):
    return a + b


@print_type
def greet(name):
    return f"Hello {name}"


add(2, 3)
greet("Max")
