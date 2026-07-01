'''
Найди индекс элемента в отсортированном массиве. Если нет — верни -1.
'''

def binary_search(nums: list[int], target: int) -> int:
    left, right = 0 , len(nums) - 1

    while left <= right: # Делим список пока можем на пары или единицы
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # ищем в правой половине
        else:
            right = mid - 1 # ищем в левой половине

    return -1

# Тесты
print(binary_search([-1,0,3,5,9,12], 9))   # 4
print(binary_search([-1,0,3,5,9,12], 2))   # -1