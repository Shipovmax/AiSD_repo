'''
Реализуйте декоратор not_null, который генерирует исключение, если декорируемая функция вернула 0.
'''


def not_null(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            raise ValueError("Ошибка: Функция вернула запрещенное значение (0)!")
        return result

    return wrapper


@not_null
def divide(a, b):
    return a / b


print(f"Результат деления: {divide(10, 2)}")

try:
    print(divide(0, 5))
except ValueError as e:
    print(f"Перехвачено исключение: {e}")
