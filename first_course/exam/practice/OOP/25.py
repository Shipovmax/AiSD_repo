'''
Создайте класс с методами для формирования вложенной последовательности
(заполнение случайными числами [-10, 10] или вводом с клавиатуры).
'''
import random


class NestedSequence:
    def __init__(self):
        self.sequence = []

    def fill_random(self, rows: int, cols: int):
        self.sequence = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

    def fill_manual(self, rows: int, cols: int):
        self.sequence = []
        for i in range(rows):
            row = []
            for j in range(cols):
                val = int(input(f"Введите элемент [{i}][{j}]: "))
                row.append(val)
            self.sequence.append(row)

    def __str__(self):
        if not self.sequence:
            return "Последовательность пуста"
        return "\n".join(str(row) for row in self.sequence)


seq = NestedSequence()

print("=== ЗАПОЛНЕНИЕ СЛУЧАЙНЫМИ ЧИСЛАМИ ===")
seq.fill_random(rows=3, cols=4)
print(seq)
print("-" * 30)

print("=== ЗАПОЛНЕНИЕ С КЛАВИАТУРЫ ===")
seq.fill_manual(rows=2, cols=2)
print(seq)
