"""
С помощью декоратора реализовать отладочный вывод работы
factorial(n) как для вызовов функций, так и для возвращаемых значений.
"""

p = 0


def printin(func):
    def wrapper(n):
        global p
        print(p * "    " + f"{func.__name__}({n})")
        p += 1
        return func(n)

    return wrapper


def printout(func):
    def wrapper(n):
        global p
        result = func(n)
        p -= 1
        print(f"{p * '    '}{result}")
        return result

    return wrapper


@printout
@printin
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("Результат:", factorial(5))
