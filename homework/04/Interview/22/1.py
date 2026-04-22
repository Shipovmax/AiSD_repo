def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    
    left = 0 
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left+1, right+1] # Так как просят 1-based
        
        elif current_sum < target:
            left += 1
        
        else:
            right -= 1

    return []

print(two_sum_sorted([1,2,3,4,5,6,7,8,9,10], 4))

'''
Время O(n)
Память O(1)
'''