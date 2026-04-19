'''
Subarray Sum Equals K
Дан массив целых чисел nums и число k. Найди
количество непрерывных подмассивов, сумма которых равна k.
Input:  nums = [1,1,1], k = 2
Output: 2

Input:  nums = [1,2,3], k = 3
Output: 2

Input:  nums = [-1,-1,1], k = -1
Output: 1
Условие: O(n) по времени. Числа могут быть
отрицательными — скользящее окно не сработает.
'''

def subarraySum(nums: list[int], k: int) -> int:
    prefix_counts = {0: 1}  # сумма 0 уже "встретилась" до начала массива
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        count += prefix_counts.get(current_sum - k, 0)
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return count