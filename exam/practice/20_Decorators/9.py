'''
Создайте функцию func(name), которая выводит имя и количество букв.
Декоратор decor_func должен возвращать имя в обратном порядке столько раз, сколько в нем букв
'''


def decor_func(func):
    def wrapper(name: str):
        func(name)

        reversed_name = name[::-1]
        letters_count = len(name)

        return [reversed_name] * letters_count

    return wrapper


@decor_func
def func(name: str):
    print(f"Имя: {name}, Количество букв: {len(name)}")


result = func("Иван")
print(f"Результат декоратора: {result}")
