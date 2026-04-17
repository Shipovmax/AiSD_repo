def sum_sub(lst: list[int]) -> int:
    if not lst:
        return 0
    head, *tail = lst
    sign = 1 if head % 2 != 0 else -1
    return sign * head + sum_sub(tail)