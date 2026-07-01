'''
Создайте функцию func() (ФИО). Декоратор decor_func возвращает ФИО в обратном порядке.
'''


def decor_func(func):
    def wrapper(*args, **kwargs):
        full_name = func(*args, **kwargs)

        words = full_name.split()
        reversed_words = words[::-1]

        return " ".join(reversed_words)

    return wrapper


@decor_func
def func():
    return "Иванов Иван Иванович"


print(func())
