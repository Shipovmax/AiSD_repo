"""
Реализуйте метод класса `Автомобиль` для сортировки списка авто по марке методом пузырька.
"""


class Automobile:
    """Класс для представления автомобиля."""

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def __repr__(self):
        return f"{self.brand} {self.model} ({self.year})"

    @classmethod
    def bubble_sort_by_brand(cls, cars):
        """
        Сортирует список автомобилей по марке (brand) методом пузырька (in-place).

        :param cars: список объектов Automobile
        """
        n = len(cars)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if cars[j].brand > cars[j + 1].brand:
                    cars[j], cars[j + 1] = cars[j + 1], cars[j]
                    swapped = True
            if not swapped:
                break


if __name__ == "__main__":
    cars = [
        Automobile("Toyota", "Camry", 2020),
        Automobile("BMW", "X5", 2019),
        Automobile("Audi", "A4", 2021),
        Automobile("Toyota", "Corolla", 2018),
        Automobile("Mercedes", "C-Class", 2022),
    ]

    print("До сортировки:")
    for car in cars:
        print(car)

    Automobile.bubble_sort_by_brand(cars)

    print("\nПосле сортировки по марке (методом пузырька):")
    for car in cars:
        print(car)
