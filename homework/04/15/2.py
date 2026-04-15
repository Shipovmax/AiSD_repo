# === ЗАДАЧА 1: FizzBuzz ===
# Для чисел от 1 до n:
# кратно 3 -> "Fizz", кратно 5 -> "Buzz", кратно 15 -> "FizzBuzz", иначе число
# Вернуть список строк.
from unittest import result


def fizzbuzz(n: int) -> list:
    result = []

    for num in range(1, n + 1):
        if num % 15 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))

    return result



# === ЗАДАЧА 2: Перевернуть строку ===
# Без срезов и reversed()

def reverse_string(s: str) -> str:
    result = ""

    for i in range(len(s) - 1, -1, -1):
        result += s[i]

    return result


# === ЗАДАЧА 3: Подсчёт вхождений символа ===
# Без count()

def char_count(s: str, char: str) -> int:
    count = 0

    for c in s:
        if c == char:
            count += 1

    return count


# === ЗАДАЧА 4: Максимум без max() ===

def find_max(nums: list) -> int:
    maximus = nums[0]

    for num in nums[1:]:
        if num > maximus:
            maximus = num

    return maximus


# === ЗАДАЧА 5: Сумма цифр числа ===

def digit_sum(n: int) -> int:
    result = 0

    for x in str(n):
        result += int(x)

    return result


# === ЗАДАЧА 6: Проверка на простое число ===

def is_prime(n: int) -> bool:
    """
    7 -> True
    10 -> False
    1 -> False
    """

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# === ЗАДАЧА 7: Убрать дубликаты из списка ===
# Сохранить порядок. Без set() напрямую на результате.

def remove_duplicates(nums: list) -> list:
    """
    [1, 2, 2, 3, 1, 4] -> [1, 2, 3, 4]
    [1, 1, 1] -> [1]
    """

    for num in nums:



# === ЗАДАЧА 8: Подсчёт слов в строке ===
# Без split()

def word_count(s: str) -> int:
    """
    "hello world foo" -> 3
    "  spaces  here  " -> 2
    """
    pass


# === ЗАДАЧА 9: Числа Фибоначчи ===
# Вернуть список первых n чисел Фибоначчи

def fibonacci(n: int) -> list:
    """
    5 -> [0, 1, 1, 2, 3]
    1 -> [0]
    """
    pass


# === ЗАДАЧА 10: Перевод в двоичную систему ===
# Без bin()

def to_binary(n: int) -> str:
    """
    10 -> "1010"
    0 -> "0"
    """
    pass


# ============================================================
# ТЕСТЫ
# ============================================================

if __name__ == "__main__":
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    print("✓ Задача 1 пройдена")

    assert reverse_string("hello") == "olleh"
    assert reverse_string("a") == "a"
    print("✓ Задача 2 пройдена")

    assert char_count("hello", "l") == 2
    assert char_count("world", "z") == 0
    print("✓ Задача 3 пройдена")

    assert find_max([3, 1, 4, 1, 5, 9]) == 9
    assert find_max([-1, -5, -2]) == -1
    print("✓ Задача 4 пройдена")

    assert digit_sum(123) == 6
    assert digit_sum(9999) == 36
    print("✓ Задача 5 пройдена")

    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(1) == False
    print("✓ Задача 6 пройдена")

    assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 1, 1]) == [1]
    print("✓ Задача 7 пройдена")

    assert word_count("hello world foo") == 3
    assert word_count("  spaces  here  ") == 2
    print("✓ Задача 8 пройдена")

    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(1) == [0]
    print("✓ Задача 9 пройдена")

    assert to_binary(10) == "1010"
    assert to_binary(0) == "0"
    print("✓ Задача 10 пройдена")

    print("\n🎯 Все тесты пройдены!")