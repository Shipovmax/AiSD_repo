'''
Longest Well-Performing Interval
День "хороший" если часов > 8. Найди длину наидлиннейшего
подмассива с числом хороших дней строго больше плохих.

Input:  hours = [9,9,6,0,6,6,9]
Output: 3

Input:  hours = [6,6,6]
Output: 0

Условие: O(n) время, O(n) память
Подсказка: замени хороший день на +1, плохой на -1 — ищешь longest subarray с суммой > 0
'''

def longest_wpi(hours: list[int]) -> int:
    pass