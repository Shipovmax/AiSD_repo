def sum_odd(lis: list[int]) -> int:
    if not lis:
        return 0
    head, *tail = lis
    return (head if head % 2 != 0 else 0) + sum_odd(tail)