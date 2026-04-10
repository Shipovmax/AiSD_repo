'''
С помощью декоратора реализовать отладочный вывод работы
factorial(n) как для вызовов функций, так и для возвращаемых значений.
'''


def debug(func):
    def wrapper(*args, **kwargs):
        print("Call:", func.__name__, args, kwargs)
        result = func(*args, **kwargs)
        print("Return:", result)
        return result

    return wrapper


@debug
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
