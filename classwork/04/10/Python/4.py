'''
Реализовать декоратор с именем not_sum, который генерирует
исключительную ситуацию, если декорируемая функция вернула
отрицательное значение суммы трех чисел.
'''


def not_sum(func):
    # func — функция, которая возвращает сумму трех чисел.
    def wrapper(*args, **kwargs):
        # Сначала считаем сумму через старую функцию.
        result = func(*args, **kwargs)

        # Если сумма меньше нуля, кидаем исключение.
        if result < 0:
            raise ValueError("Sum is negative")

        # Если сумма нормальная, возвращаем ее.
        return result

    return wrapper


# sum_three теперь работает через проверку not_sum.
@not_sum
def sum_three(a, b, c):
    return a + b + c


try:
    # Тут сумма отрицательная: 1 + 2 - 10 = -7.
    print(sum_three(1, 2, -10))
except ValueError:
    # Поэтому попадаем сюда.
    print("ValueError")
