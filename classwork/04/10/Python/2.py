'''
Реализовать декоратор с именем not_none, который генерирует
исключительную ситуацию если декорируемая функция вернула значения None.
'''

def not_none(func):
    # func — это функция, результат которой будем проверять.
    def wrapper(*args, **kwargs):
        # Сначала вызываем обычную функцию.
        result = func(*args, **kwargs)

        # Если функция вернула None, кидаем исключение.
        if result is None:
            raise AttributeError("Function returned None")

        # Если все нормально, возвращаем результат.
        return result

    return wrapper


# add теперь будет работать через not_none.
@not_none
def add(a, b):
    # c считается просто для примера, но дальше специально возвращается None.
    c = a + b
    return None


try:
    # Тут будет ошибка, потому что add вернет None.
    add(1, 2)
except AttributeError:
    # Сюда попадем после ошибки.
    print("AttributeError")
