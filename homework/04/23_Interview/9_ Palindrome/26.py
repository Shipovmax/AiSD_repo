"""
Определи, является ли строка палиндромом
(игнорируй не-алфавитные символы, регистр).
"""


def is_palindrome(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


# Two pointers версия — O(1) доп. память
def is_palindrome_v2(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


print(is_palindrome_v2("A man, a plan, a canal: Panama"))  # True
print(is_palindrome_v2("race a car"))  # False
