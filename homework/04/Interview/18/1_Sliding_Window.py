"""
Longest Substring Without Repeating Characters
Дана строка s. Найди длину наидлиннейшей подстроки
без повторяющихся символов.
Input:  s = "abcabcbb"
Output: 3  # "abc"

Input:  s = "pwwkew"
Output: 3  # "wke"

Input:  s = ""
Output: 0
Условия: решение за O(n), без встроенных функций
типа collections.Counter для основной логики.
"""


def length_of_longest_substring(s: str) -> int:
    if not s:  # Краевой случай s = ""
        return 0

    seen = {}
    left = 0
    max_len = 0

    for i, char in enumerate(s):
        if (
            char in seen and seen[char] >= left
        ):  # Проверка есть ли символ в текущем окне
            left = seen[char] + 1  # Сдвигаем левую границу окна вправо
        seen[char] = i  # Запоминаем позицию
        max_len = max(max_len, i - left + 1)  # Обновляем максимум

    return max_len


print("Сложность O(n)")
print(length_of_longest_substring("zxczxcasdzxc"))  # Тест
