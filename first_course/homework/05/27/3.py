def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Начальный шаг (расстояние между сравниваемыми элементами)

    while gap > 0:
        # Делаем обычную сортировку вставками, но с шагом gap вместо 1
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Сравниваем элементы на расстоянии gap
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        # Уменьшаем шаг в два раза для следующего прохода
        gap //= 2
    return arr
