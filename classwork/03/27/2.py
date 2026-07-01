"""
Шипов Максим Кириллович

Вариант 2
Задание 2


Построить базовый класс с указанными в таблице полями и методами:
конструктор; функция, которая определяет «качество» объекта - Q по заданной формуле;
метод вывода информации об объекте. Построить дочерний класс (класс-потомок), который
содержит: дополнительное поле Р; функцию, которая определяет «качество» объекта дочернего
класса - Ор и перегружает функцию качества родительского класса (2), выполняя вычисление
по новой формуле. Создать проект для демонстрации работы: ввод и вывод информации об объектах классов.

"""


class Computer:
    def __init__(self, cpu_name: str, cpu_frequency: int, ram_size: int):
        self.cpu_name = cpu_name
        self.cpu_frequency = cpu_frequency
        self.ram_size = ram_size

    def get_quality(self) -> float:
        return (0.1 * self.cpu_frequency) + self.ram_size

    def display(self) -> str:
        return (
            f"Компьютер:\n"
            f"  Процессор: {self.cpu_name}\n"
            f"  Частота: {self.cpu_frequency} МГц\n"
            f"  ОЗУ: {self.ram_size} Мб\n"
            f"  Качество (Q): {self.get_quality():.2f}"
        )


class ComputerWithSSD(Computer):
    def __init__(self, cpu_name: str, cpu_frequency: int, ram_size: int, ssd_size: int):
        super().__init__(cpu_name, cpu_frequency, ram_size)
        self.ssd_size = ssd_size

    def get_quality(self) -> float:
        return 2 + 0.5 * self.ssd_size

    def display(self) -> str:
        return (
            f"Компьютер с SSD:\n"
            f"  Процессор: {self.cpu_name}\n"
            f"  Частота: {self.cpu_frequency} МГц\n"
            f"  ОЗУ: {self.ram_size} Мб\n"
            f"  SSD: {self.ssd_size} Гб\n"
            f"  Качество (Op): {self.get_quality():.2f}"
        )


if __name__ == "__main__":
    print("=== Демонстрация работы базового класса ===\n")

    # Ввод данных для базового класса
    print("Ввод данных для компьютера:")
    cpu_name = input("  Наименование процессора: ")
    cpu_freq = int(input("  Тактовая частота (МГц): "))
    ram = int(input("  Объем ОЗУ (Мб): "))

    comp = Computer(cpu_name, cpu_freq, ram)

    print("\n" + comp.display())

    print("\n\n=== Демонстрация работы дочернего класса ===\n")

    # Ввод данных для дочернего класса
    print("Ввод данных для компьютера с SSD:")
    cpu_name2 = input("  Наименование процессора: ")
    cpu_freq2 = int(input("  Тактовая частота (МГц): "))
    ram2 = int(input("  Объем ОЗУ (Мб): "))
    ssd = int(input("  Объем SSD (Гб): "))

    comp_ssd = ComputerWithSSD(cpu_name2, cpu_freq2, ram2, ssd)

    print("\n" + comp_ssd.display())

    print("\n\n=== Сравнение качества ===\n")
    print(f"Качество базового компьютера: {comp.get_quality():.2f}")
    print(f"Качество компьютера с SSD: {comp_ssd.get_quality():.2f}")
