'''
Создайте класс Fruit (форма, цвет, вкус).
Реализуйте методы подсчета общего веса, сравнение веса с другим экземпляром и вывод информации в виде таблицы.
'''


class Fruit:
    def __init__(self, shape: str, color: str, taste: str, weights: list[float] = None):
        self.shape = shape
        self.color = color
        self.taste = taste
        self.weights = weights if weights is not None else []

    def get_total_weight(self) -> float:
        return sum(self.weights)

    def __eq__(self, other) -> bool:
        if isinstance(other, Fruit):
            return self.get_total_weight() == other.get_total_weight()
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Fruit):
            return self.get_total_weight() < other.get_total_weight()
        return False

    def __str__(self) -> str:
        header = f"| {'Форма':<12} | {'Цвет':<10} | {'Вкус':<12} | {'Общий вес (г)':<14} |"
        divider = f"|{'-' * 14}|{'-' * 12}|{'-' * 14}|{'-' * 16}|"
        row = f"| {self.shape:<12} | {self.color:<10} | {self.taste:<12} | {self.get_total_weight():<14.1f} |"
        return f"{header}\n{divider}\n{row}"


apple = Fruit("Круглая", "Красный", "Сладкий", [150.0, 180.0, 165.0])
banana = Fruit("Продолговатая", "Желтый", "Сладкий", [120.0, 130.0, 115.0, 140.0])

print("=== ИНФОРМАЦИЯ О ЯБЛОКЕ ===")
print(apple)
print("\n=== ИНФОРМАЦИЯ О БАНАНЕ ===")
print(banana)

print("\n=== СРАВНЕНИЕ ВЕСА ===")
print(f"Вес яблок ({apple.get_total_weight()}г) равен весу бананов ({banana.get_total_weight()}г)? {apple == banana}")
print(f"Вес яблок меньше веса бананов? {apple < banana}")
