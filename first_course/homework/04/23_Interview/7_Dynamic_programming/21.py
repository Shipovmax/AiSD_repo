"""
Найди подмассив с максимальной суммой
"""


def max_subarray(nums: list[int]) -> int:
    max_sum     = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum     = max(max_sum, current_sum)

    return max_sum


# Тест
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 (4,-1,2,1)
print(max_subarray([1]))  # 1
print(max_subarray([5, 4, -1, 7, 8]))  # 23
