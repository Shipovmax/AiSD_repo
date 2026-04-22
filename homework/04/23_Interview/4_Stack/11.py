"""
Дана строка из скобок ()[]{}.
Определи, является ли она валидной.
"""


def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in mapping:
            if stack:  # если стек не пустой
                top = stack.pop()  # берём верхний элемент
            else:
                top = "#"  # иначе ставим заглушку

            if mapping[char] != top:
                return False

        else:
            stack.append(char)

    return len(stack) == 0


# Тесты
print(is_valid("()[]{}"))  # True
print(is_valid("([)]"))    # False
print(is_valid("{[]}"))    # True
