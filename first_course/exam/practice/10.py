'''
Создайте класс ТОВАР с методами вывода информации и проверки соответствия условиям.

Реализуйте дочерние классы:

ЭЛЕКТРОНИКА (название, производитель, цена, тип устройства)
ОДЕЖДА (название, производитель, цена, размер)
ПРОДУКТЫ ПИТАНИЯ (название, производитель, цена, срок годности)

Дополнительно: Создайте список товаров, выведите всю базу и организуйте поиск по названию или цене.
'''


class Product:
    def __init__(self, name: str, manufacturer: str, price: float, product_type: str):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.product_type = product_type

    def __str__(self):
        return (f"Товар: {self.name}\n"
                f"Производитель: {self.manufacturer}\n"
                f"Цена: {self.price} руб.\n"
                f"Категория: {self.product_type}")


class Electronics(Product):
    def __init__(self, name: str, manufacturer: str, price: float, device_type: str):
        super().__init__(name, manufacturer, price, "Электроника")
        self.device_type = device_type

    def __str__(self):
        return super().__str__() + f"\nТип устройства: {self.device_type}\n{'-' * 30}"


class Clothing(Product):
    def __init__(self, name: str, manufacturer: str, price: float, size: str):
        super().__init__(name, manufacturer, price, "Одежда")
        self.size = size

    def __str__(self):
        return super().__str__() + f"\nРазмер: {self.size}\n{'-' * 30}"


class Food(Product):
    def __init__(self, name: str, manufacturer: str, price: float, expiration_date: str):
        super().__init__(name, manufacturer, price, "Продукты питания")
        self.expiration_date = expiration_date

    def __str__(self):
        return super().__str__() + f"\nСрок годности: {self.expiration_date}\n{'-' * 30}"


def search_products(database, name: str = None, price: float = None):
    results = []
    for item in database:
        if name and name.lower() not in item.name.lower():
            continue
        if price and item.price != price:
            continue
        results.append(item)
    return results


products_database = [
    Electronics("iPhone 15", "Apple", 85000.0, "Смартфон"),
    Clothing("Футболка", "Nike", 2500.0, "L"),
    Food("Молоко", "Простоквашино", 90.0, "15.06.2026"),
    Electronics("MacBook Air", "Apple", 120000.0, "Ноутбук"),
    Clothing("Куртка", "Adidas", 8500.0, "M")
]

print("=== ВСЯ БАЗА ТОВАРОВ ===")
for product in products_database:
    print(product)

print("\n" + "=" * 40 + "\n")

print("=== ПОИСК: По названию 'iPhone' ===")
found_by_name = search_products(products_database, name="iPhone")
for product in found_by_name:
    print(product)

print("=== ПОИСК: По цене '2500.0 руб.' ===")
found_by_price = search_products(products_database, price=2500.0)
for product in found_by_price:
    print(product)
