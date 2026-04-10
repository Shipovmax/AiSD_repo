'''
Реализовать декоратор, который выводит на печать возвращаемые значения функции.
'''


def print_return(func):
    # func — это функция, которую мы декорируем.
    def wrapper(*args, **kwargs):
        # Вызываем старую функцию с теми же аргументами.
        result = func(*args, **kwargs)
        # Печатаем то, что она вернула.
        print("Return:", result)
        # Возвращаем результат, чтобы функция продолжала нормально работать.
        return result

    # Возвращаем новую функцию вместо старой.
    return wrapper


# Декоратор заменит add на wrapper.
@print_return
def add(a, b):
    return a + b


# Декоратор заменит greet на wrapper.
@print_return
def greet(name):
    return f"Hello {name}"


# Тут вызываются уже обернутые функции.
add(2, 3)
greet("Max")
