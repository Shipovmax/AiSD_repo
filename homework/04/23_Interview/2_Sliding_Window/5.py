def max_sum_subarray(arr: list[int], k: int) -> int:
    """
    Дан массив и число k. Найди максимальную сумму подмассива длины ровно k.
    """

    if len(arr) < k:
        return -1

    # Сумма первого массива
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Скользим
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Тесты
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9 (5+1+3)
print(max_sum_subarray([2, 3, 4, 1, 5], 2))  # 7 (3+4)
