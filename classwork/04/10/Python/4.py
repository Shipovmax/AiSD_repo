'''
Реализовать декоратор с именем not_sum, который генерирует
исключительную ситуацию, если декорируемая функция вернула
отрицательное значение суммы трех чисел.
'''


def not_sum(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result < 0:
            raise ValueError("Sum is negative")

        return result

    return wrapper


@not_sum
def sum_three(a, b, c):
    return a + b + c


try:
    print(sum_three(1, 2, -10))
except ValueError:
    print("ValueError")
