"""
Дан набор монет и сумма amount.
Найди минимальное количество монет для набора суммы.
Если невозможно — верни -1.
"""


def coin_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Тест
print(coin_change([1, 5, 11], 15))  # 3 (5+5+5)
print(coin_change([2], 3))           # -1
print(coin_change([1, 2, 5], 11))   # 3 (5+5+1)