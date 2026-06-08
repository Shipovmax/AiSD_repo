'''
Создайте декоратор tol(dlina, fill).
Он превращает результат функции в словарь из dlina элементов.
Если элементов меньше, заполняет их значением fill.
Если больше — обрезает хвост.
'''


def tol(dlina: int, fill=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = list(func(*args, **kwargs))

            if len(result) < dlina:
                result.extend([fill] * (dlina - len(result)))
            else:
                result = result[:dlina]

            return {i: val for i, val in enumerate(result)}

        return wrapper

    return decorator


@tol(dlina=5, fill="-")
def get_short_list():
    return ["яблоко", "банан", "груша"]


@tol(dlina=3, fill="пусто")
def get_long_list():
    return [10, 20, 30, 40, 50, 60]


print("=== ТЕСТ 1 (Заполнение) ===")
print(get_short_list())

print("\n=== ТЕСТ 2 (Обрезка) ===")
print(get_long_list())
