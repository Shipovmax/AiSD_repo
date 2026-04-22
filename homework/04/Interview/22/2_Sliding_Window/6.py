def min_subarray_len(target: int, nums: list[int]) -> int:
    '''
    Дан массив положительных чисел и target. 
    Найди минимальную длину подмассива с суммой >= target.
    '''

    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        # Сужаем окно пока условие выполняется
        while current_sum >= target:
            min_len     = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left        += 1
    
    return min_len if min_len != float('inf') else 0

# Тест
print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))  # 2 (4+3)
print(min_subarray_len(4, [1, 4, 4]))             # 1 (4)