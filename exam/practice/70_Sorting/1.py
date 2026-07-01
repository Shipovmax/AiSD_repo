"""
Реализуйте сортировку списка городов по населению методом Шелла.
"""


class City:
    """Класс для представления города."""

    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __repr__(self):
        return f"{self.name} ({self.population})"


def shell_sort(arr, key=None):
    """
    Сортировка списка методом Шелла (in-place).

    :param arr: список элементов для сортировки
    :param key: функция, извлекающая значение для сравнения (по умолчанию сам элемент)
    """
    if key is None:
        key = lambda x: x

    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and key(arr[j - gap]) > key(temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


if __name__ == "__main__":
    cities = [
        City("Москва", 12_000_000),
        City("Санкт-Петербург", 5_400_000),
        City("Новосибирск", 1_600_000),
        City("Екатеринбург", 1_500_000),
        City("Казань", 1_200_000),
        City("Нижний Новгород", 1_250_000),
    ]

    print("До сортировки:")
    print(cities)

    shell_sort(cities, key=lambda city: city.population)

    print("\nПосле сортировки по населению (метод Шелла):")
    print(cities)
