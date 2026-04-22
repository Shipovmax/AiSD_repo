def max_area(height: list[int]) -> int:
    '''
    Дан массив высот. Найди два столбца, между 
    которыми помещается максимум воды. 
    Вода = min(h[l], h[r]) * (r - l).
    '''

    left, right = 0, len(height) - 1 
    max_water    = 0

    while left < right:
        water    = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, water)

        if height[left] < height[right]:
            left  += 1
        else:
            right -= 1

    return max_water

# Тест 
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))

'''
Время  O(n)
Память O(1)
'''