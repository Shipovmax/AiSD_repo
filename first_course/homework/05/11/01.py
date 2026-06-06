class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Если ряд всего один или строка короче количества рядов,
        # зигзаг невозможен и не нужен
        if numRows == 1 or numRows >= len(s):
            return s

        # Создаем список строк для каждого ряда
        rows = [""] * numRows
        current_row = 0
        step = 1  # 1 означает движение вниз, -1 — вверх

        for char in s:
            rows[current_row] += char

            # Если дошли до края (верхнего или нижнего), меняем направление
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1

            current_row += step

        # Соединяем все ряды в одну итоговую строку
        return "".join(rows)
