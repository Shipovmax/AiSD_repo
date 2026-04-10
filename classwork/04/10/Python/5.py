'''
С помощью декоратора реализовать отладочный вывод работы
factorial(n) как для вызовов функций, так и для возвращаемых значений.
'''


def debug(func):
    # func — функция, вызовы и возвраты которой надо показать.
    def wrapper(*args, **kwargs):
        # Печатаем имя функции и аргументы перед вызовом.
        print("Call:", func.__name__, args, kwargs)
        # Вызываем настоящую функцию.
        result = func(*args, **kwargs)
        # Печатаем то, что функция вернула.
        print("Return:", result)
        # Возвращаем результат дальше.
        return result

    return wrapper


# factorial теперь будет печатать каждый вызов и каждый возврат.
@debug
def factorial(n):
    # База рекурсии: factorial(0) и factorial(1) равны 1.
    if n == 0 or n == 1:
        return 1

    # Рекурсивный шаг: n! = n * (n - 1)!.
    return n * factorial(n - 1)


# Запускаем пример.
print(factorial(5))
