'''
Реализовать декоратор с именем print_type, выводящий
на печать тип значения, возвращаемого декорируемой функцией.
'''


def print_type(func):
    # func — функция, тип результата которой надо вывести.
    def wrapper(*args, **kwargs):
        # Вызываем функцию и сохраняем ее результат.
        result = func(*args, **kwargs)
        # Печатаем тип результата.
        print("Type:", type(result))
        # Возвращаем сам результат.
        return result

    return wrapper


# add теперь будет печатать тип результата.
@print_type
def add(a, b):
    return a + b


# greet тоже будет печатать тип результата.
@print_type
def greet(name):
    return f"Hello {name}"


# Проверяем декоратор на числе и строке.
add(2, 3)
greet("Max")
