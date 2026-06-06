"""
Метод Ньютона для вычисления квадратного корня

Найти sqrt(n) с заданной точностью (epsilon)
"""


def recursive_sqrt(n: float, guess: float = 1.0, epsilon: float = 1e-7) -> float:

    # Базовый случай: если разница между guess^2 и n меньше точности, мы нашли корень
    if abs(guess * guess - n) < epsilon:
        return guess

    # Рекурсия функции, для следующего приближения к числу
    next_guess = (guess + n / guess) / 2
    return recursive_sqrt(n, next_guess, epsilon)
