# ============================================================
# БЛОК 2: 10 ЗАДАЧ НА PYTHON (уровень junior)
# ============================================================


# === ЗАДАЧА 1: Анаграммы ===
# Две строки являются анаграммами, если состоят из одних и тех же символов
# в одном и том же количестве, но (возможно) в разном порядке.
# Регистр НЕ важен: "Listen" и "Silent" — анаграммы.
# Пробелы НЕ учитываются.
# Без использования sorted() и Counter.
#
# Примеры:
#   is_anagram("listen", "silent") -> True
#   is_anagram("Hello", "world")   -> False
#   is_anagram("Astronomer", "Moon starer") -> True


def is_anagram(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    freq = {}

    for c in s1:
        freq[c] = freq.get(c, 0) + 1

    for c in s2:
        if c not in freq or freq[c] == 0:
            return False
        freq[c] -= 1

    return True


# === ЗАДАЧА 2: Палиндром ===
# Строка является палиндромом, если читается одинаково слева направо и справа налево.
# Учитывать только буквы и цифры, игнорировать пробелы, знаки препинания и регистр.
# Без срезов (s[::-1]) и reversed().
#
# Примеры:
#   is_palindrome("racecar")              -> True
#   is_palindrome("A man a plan a canal Panama") -> True
#   is_palindrome("hello")                -> False


def is_palindrome(s: str) -> bool:
    cleaned = ""

    for c in s:
        if c.isalnum():
            cleaned += c.lower()

    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


# === ЗАДАЧА 3: Две суммы (Two Sum) ===
# Дан список целых чисел nums и целевое число target.
# Найти индексы двух чисел, сумма которых равна target.
# Гарантируется ровно одно решение. Один элемент нельзя использовать дважды.
# Решить за O(n) — то есть без вложенных циклов.
#
# Примеры:
#   two_sum([2, 7, 11, 15], 9)  -> [0, 1]   (2 + 7 = 9)
#   two_sum([3, 2, 4], 6)       -> [1, 2]   (2 + 4 = 6)
#   two_sum([3, 3], 6)          -> [0, 1]


def two_sum(nums: list, target: int) -> list:
    seen = {}  # значение -> индекс

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


# === ЗАДАЧА 4: Группировка по первой букве ===
# Дан список слов. Сгруппировать слова по первой букве (lowercase).
# Вернуть словарь: ключ — буква, значение — список слов в порядке появления.
# Слова с одинаковым первым символом объединяются в один список.
#
# Примеры:
#   group_by_first_letter(["apple", "ant", "banana", "avocado", "blueberry"])
#   -> {"a": ["apple", "ant", "avocado"], "b": ["banana", "blueberry"]}
#
#   group_by_first_letter([]) -> {}


def group_by_first_letter(words: list) -> dict:
    result = {}

    for word in words:
        key = word[0].lower()
        if key not in result:
            result[key] = []
        result[key].append(word)

    return result


# === ЗАДАЧА 5: Сжатие строки (Run-Length Encoding) ===
# Сжать строку методом RLE: заменить последовательности одинаковых символов
# на символ + количество повторений. Если символ встречается 1 раз — число не добавлять.
# Если сжатая строка длиннее или равна исходной — вернуть исходную.
#
# Примеры:
#   compress("aabcccdddd")  -> "a2bc3d4"
#   compress("abc")         -> "abc"        (сжатие не даёт выигрыша)
#   compress("aaaa")        -> "a4"


def compress(s: str) -> str:
    if not s:
        return s

    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + (str(count) if count > 1 else "")
            count = 1

    result += s[-1] + (str(count) if count > 1 else "")

    return result if len(result) < len(s) else s


# === ЗАДАЧА 6: Валидность скобок ===
# Дана строка, содержащая символы: '(', ')', '{', '}', '[', ']'.
# Строка валидна, если:
#   1. Каждая открывающая скобка закрыта скобкой того же типа.
#   2. Скобки закрываются в правильном порядке (вложенность соблюдена).
# Использовать стек (список как стек).
#
# Примеры:
#   is_valid_brackets("()")        -> True
#   is_valid_brackets("()[]{}")    -> True
#   is_valid_brackets("(]")        -> False
#   is_valid_brackets("([)]")      -> False
#   is_valid_brackets("{[]}")      -> True


def is_valid_brackets(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else None
            if top != mapping[char]:
                return False
        else:
            stack.append(char)

    return len(stack) == 0


# === ЗАДАЧА 7: Разворот слов в строке ===
# Дана строка из слов, разделённых пробелами.
# Вернуть строку, где слова идут в обратном порядке.
# Несколько пробелов между словами и по краям — схлопнуть в один.
# Без split() и reversed().
#
# Примеры:
#   reverse_words("hello world")       -> "world hello"
#   reverse_words("  the sky  is blue  ") -> "blue is sky the"
#   reverse_words("one")               -> "one"


def reverse_words(s: str) -> str:
    words = []
    word = ""

    for c in s:
        if c != " ":
            word += c
        else:
            if word:
                words.append(word)
                word = ""

    if word:
        words.append(word)

    result = ""

    for i in range(len(words) - 1, -1, -1):
        result += words[i]
        if i > 0:
            result += " "

    return result


# === ЗАДАЧА 8: Матрица — поворот на 90° по часовой ===
# Дана квадратная матрица N×N (список списков).
# Повернуть её на 90 градусов по часовой стрелке IN-PLACE (изменить переданную матрицу).
# Алгоритм: сначала транспонировать, потом отразить каждую строку горизонтально.
# Вернуть изменённую матрицу.
#
# Пример для 3×3:
#   Исходная:        После поворота:
#   1 2 3            7 4 1
#   4 5 6    ->      8 5 2
#   7 8 9            9 6 3


def rotate_matrix(matrix: list) -> list:
    n = len(matrix)

    # Шаг 1: транспонирование (matrix[i][j] <-> matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Шаг 2: горизонтальное отражение каждой строки
    for i in range(n):
        left, right = 0, n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1

    return matrix


# === ЗАДАЧА 9: Число Армстронга ===
# Число является числом Армстронга (нарциссическим числом), если сумма его цифр,
# возведённых в степень количества цифр, равна самому числу.
# Например: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 — число Армстронга.
# Вернуть список всех чисел Армстронга в диапазоне [start, end] включительно.
#
# Примеры:
#   armstrong_numbers(1, 500)   -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
#   armstrong_numbers(100, 200) -> [153]


def armstrong_numbers(start: int, end: int) -> list:
    result = []

    for n in range(start, end + 1):
        digits = str(n)
        power = len(digits)
        total = sum(int(d) ** power for d in digits)
        if total == n:
            result.append(n)

    return result


# === ЗАДАЧА 10: Наибольший общий делитель и наименьшее общее кратное ===
# Реализовать две функции:
#
# gcd(a, b) — наибольший общий делитель двух натуральных чисел.
#   Использовать алгоритм Евклида (рекурсивный или итеративный).
#   Алгоритм: gcd(a, b) = gcd(b, a % b), база: gcd(a, 0) = a
#
# lcm(a, b) — наименьшее общее кратное двух натуральных чисел.
#   Формула: lcm(a, b) = a * b // gcd(a, b)
#
# Примеры:
#   gcd(48, 18) -> 6
#   gcd(100, 75) -> 25
#   lcm(4, 6)   -> 12
#   lcm(7, 5)   -> 35


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


# ============================================================
# ТЕСТЫ
# ============================================================

if __name__ == "__main__":
    # --- Задача 1: Анаграммы ---
    assert is_anagram("listen", "silent") == True
    assert is_anagram("Hello", "world") == False
    assert is_anagram("Astronomer", "Moon starer") == True
    assert is_anagram("abc", "ab") == False
    assert is_anagram("a", "a") == True
    assert is_anagram("Dormitory", "Dirty room") == True
    print("✓ Задача 1 пройдена")

    # --- Задача 2: Палиндром ---
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("Was it a car or a cat I saw") == True
    assert is_palindrome("No lemon no melon") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False
    print("✓ Задача 2 пройдена")

    # --- Задача 3: Two Sum ---
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 5, 3, 7], 8) == [1, 2]
    assert two_sum([-1, -2, -3, -4], -6) == [1, 3]
    print("✓ Задача 3 пройдена")

    # --- Задача 4: Группировка по первой букве ---
    assert group_by_first_letter(
        ["apple", "ant", "banana", "avocado", "blueberry"]
    ) == {"a": ["apple", "ant", "avocado"], "b": ["banana", "blueberry"]}
    assert group_by_first_letter([]) == {}
    assert group_by_first_letter(["Zoo", "zebra", "ant"]) == {
        "z": ["Zoo", "zebra"],
        "a": ["ant"],
    }
    assert group_by_first_letter(["one"]) == {"o": ["one"]}
    print("✓ Задача 4 пройдена")

    # --- Задача 5: Сжатие строки ---
    assert compress("aabcccdddd") == "a2bc3d4"
    assert compress("abc") == "abc"
    assert compress("aaaa") == "a4"
    assert compress("") == ""
    assert compress("aabbcc") == "aabbcc"  # "a2b2c2" — не короче, возвращаем исходную
    assert compress("aaabbb") == "a3b3"
    assert compress("a") == "a"
    print("✓ Задача 5 пройдена")

    # --- Задача 6: Валидность скобок ---
    assert is_valid_brackets("()") == True
    assert is_valid_brackets("()[]{}") == True
    assert is_valid_brackets("(]") == False
    assert is_valid_brackets("([)]") == False
    assert is_valid_brackets("{[]}") == True
    assert is_valid_brackets("") == True
    assert is_valid_brackets("(((") == False
    assert is_valid_brackets("]") == False
    print("✓ Задача 6 пройдена")

    # --- Задача 7: Разворот слов ---
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("  the sky  is blue  ") == "blue is sky the"
    assert reverse_words("one") == "one"
    assert reverse_words("  spaces  ") == "spaces"
    assert reverse_words("a b c") == "c b a"
    print("✓ Задача 7 пройдена")

    # --- Задача 8: Поворот матрицы ---
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert rotate_matrix(m1) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    m2 = [[1, 2], [3, 4]]
    assert rotate_matrix(m2) == [[3, 1], [4, 2]]

    m3 = [[5]]
    assert rotate_matrix(m3) == [[5]]

    m4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    assert rotate_matrix(m4) == [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]
    print("✓ Задача 8 пройдена")

    # --- Задача 9: Числа Армстронга ---
    assert armstrong_numbers(1, 9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert armstrong_numbers(100, 200) == [153]
    assert armstrong_numbers(1, 500) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
    assert armstrong_numbers(400, 410) == [407]
    assert armstrong_numbers(10, 100) == []
    print("✓ Задача 9 пройдена")

    # --- Задача 10: GCD и LCM ---
    assert gcd(48, 18) == 6
    assert gcd(100, 75) == 25
    assert gcd(7, 5) == 1
    assert gcd(12, 12) == 12
    assert gcd(0, 5) == 5

    assert lcm(4, 6) == 12
    assert lcm(7, 5) == 35
    assert lcm(12, 18) == 36
    assert lcm(1, 100) == 100
    assert lcm(6, 6) == 6
    print("✓ Задача 10 пройдена")

    print("\n🎯 Все тесты пройдены!")
