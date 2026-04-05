# =============================================================================
# Задание 1.1: Глобальная переменная и вывод отладочной информации
# =============================================================================

_recursion_depth = 0


def factorial_with_debug(n):
    global _recursion_depth

    print("    " * _recursion_depth + f"factorial({n})")
    _recursion_depth += 1

    if n == 0:
        _recursion_depth -= 1
        return 1

    result = n * factorial_with_debug(n - 1)
    _recursion_depth -= 1
    return result


# =============================================================================
# Задание 1.2: Функции printIn(s) и printOut(s)
# =============================================================================

def printIn(s):
    global _recursion_depth
    print("    " * _recursion_depth + s)
    _recursion_depth += 1


def printOut(s):
    global _recursion_depth
    _recursion_depth -= 1
    print("    " * _recursion_depth + s)


# =============================================================================
# Задание 1.3: factorial(n) с использованием printIn(s) и printOut(s)
# =============================================================================

def factorial_recursive(n):
    printIn(f"factorial({n})")

    if n == 0:
        printOut("1")
        return 1

    result = n * factorial_recursive(n - 1)
    printOut(str(result))
    return result


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial(n):
    global _recursion_depth
    _recursion_depth = 0
    return factorial_recursive(n)


# =============================================================================
# Тестирование
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Задание 1.1: factorial_with_debug(4)")
    print("=" * 60)
    _recursion_depth = 0
    result = factorial_with_debug(4)
    print(f"\nРезультат: {result}\n")

    print("=" * 60)
    print("Задание 1.3: factorial(4) с printIn/printOut")
    print("=" * 60)
    print("In: factorial(4)")
    factorial(4)

    print("\n" + "=" * 60)
    print("Итеративная версия: factorial_iterative(4)")
    print("=" * 60)
    print(f"Результат: {factorial_iterative(4)}")

