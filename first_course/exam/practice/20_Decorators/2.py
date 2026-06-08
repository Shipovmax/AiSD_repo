'''
Реализуйте декоратор, который возводит число в квадрат, если оно четное, и в куб, если нечетное.
'''


def sq_or_trio(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result % 2 == 0:
            return result ** 2
        else:
            return result ** 3

    return wrapper


@sq_or_trio
def check(a, b):
    return a + b


print(f"Результат для (2, 4): {check(2, 4)}")

print(f"Результат для (1, 2): {check(1, 2)}")
