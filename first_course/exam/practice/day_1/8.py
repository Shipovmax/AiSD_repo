'''
Создайте класс РЕСТОРАН с методами вывода информации и проверки соответствия условиям.

Реализуйте дочерние классы:

ИТАЛЬЯНСКИЙ РЕСТОРАН (название, адрес, тип кухни, рейтинг)
ЯПОНСКИЙ РЕСТОРАН (название, адрес, тип кухни, рейтинг)
ФРАНЦУЗСКИЙ РЕСТОРАН (название, адрес, тип кухни, рейтинг)

ДОПОЛНИТЕЛЬНО: Создайте список ресторанов, выведите всю базу и организуйте поиск по типу кухни или рейтингу.
'''


class Restaurant:
    def __init__(self, name: str, address: str, kitchen_type: str, rating: float):
        self.name = name
        self.address = address
        self.kitchen_type = kitchen_type
        self.rating = rating

    def __str__(self):
        return (f"Ресторан   -> {self.name}\n"
                f"Находится  -> {self.address}\n"
                f"Тип кухни  -> {self.kitchen_type}\n"
                f"Рейтинг    -> {self.rating}\n"
                f"{'-' * 30}")

    def is_highly_rated(self) -> bool:
        return self.rating >= 4.5


class ItalianRestaurant(Restaurant):
    def __init__(self, name: str, address: str, rating: float):
        super().__init__(name, address, "Итальянская", rating)


class JapaneseRestaurant(Restaurant):
    def __init__(self, name: str, address: str, rating: float):
        super().__init__(name, address, "Японская", rating)


class FrenchRestaurant(Restaurant):
    def __init__(self, name: str, address: str, rating: float):
        super().__init__(name, address, "Французская", rating)


# 1. Создаем список (базу данных) ресторанов
restaurant_database = [
    ItalianRestaurant("Mama Mia", "ул. Римская, 10", 4.7),
    JapaneseRestaurant("Тануки", "ул. Токийская, 5", 4.3),
    FrenchRestaurant("Le Petit", "ул. Парижская, 24", 4.8),
    ItalianRestaurant("Piazza", "ул. Неапольская, 2", 4.1),
    JapaneseRestaurant("Суши Мастер", "ул. Самураев, 18", 4.6)
]

print("=== ВСЯ БАЗА РЕСТОРАНОВ ===")
for rest in restaurant_database:
    print(rest)

print("\n" + "=" * 30 + "\n")


def search_restaurants(database, kitchen: str = None, min_rating: float = None):
    results = []

    for rest in database:
        if kitchen and rest.sport_type.lower() != kitchen.lower():
            continue
        if min_rating and rest.rating < min_rating:
            continue

        results.append(rest)

    return results


print("=== ПОИСК: Итальянская кухня ===")
italian_kitchen = search_restaurants(restaurant_database, kitchen="Итальянская")
for rest in italian_kitchen:
    print(rest)

print("=== ПОИСК: Рейтинг от 4.6 и выше ===")
top_rated = search_restaurants(restaurant_database, min_rating=4.6)
for rest in top_rated:
    print(rest)
