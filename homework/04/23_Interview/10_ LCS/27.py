"""
Найди длину самой длинной общей подпоследовательности двух строк.
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * n(n + 1) for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1 ):
            if text1[]