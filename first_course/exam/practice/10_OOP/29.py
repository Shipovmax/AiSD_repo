'''
Создайте класс ТОВАР (информация, доступность для покупателя с заданной суммой).
Дочерние классы: ПРОДУКТ, ПАРТИЯ, ТЕЛЕФОН. Организуйте поиск по цене
'''


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def is_affordable(self, budget: float) -> bool:
        return budget >= self.price

    def __str__(self):
        return f"Товар: {self.name} | Цена: {self.price} руб."


class FoodProduct(Product):
    def __init__(self, name: str, price: float, expiration_date: str):
        super().__init__(name, price)
        self.expiration_date = expiration_date

    def __str__(self):
        return f"Продукт: {self.name} | Цена: {self.price} руб. | Срок годности: {self.expiration_date}"


class Batch(Product):
    def __init__(self, name: str, price_per_item: float, count: int):
        total_price = price_per_item * count
        super().__init__(name, total_price)
        self.price_per_item = price_per_item
        self.count = count

    def __str__(self):
        return f"Партия: {self.name} | Кол-во: {self.count} шт. | Общая цена: {self.price} руб. (за шт: {self.price_per_item} руб.)"


class Phone(Product):
    def __init__(self, name: str, price: float, ram: int):
        super().__init__(name, price)
        self.ram = ram

    def __str__(self):
        return f"Телефон: {self.name} | Цена: {self.price} руб. | ОЗУ: {self.ram} ГБ"


def search_by_max_price(catalog: list[Product], max_price: float) -> list[Product]:
    return [item for item in catalog if item.price <= max_price]


catalog = [
    FoodProduct("Торт", 800.0, "12.06.2026"),
    Phone("Xiaomi RedMi", 18000.0, 8),
    Batch("Канцелярские наборы", 150.0, 50),  # 150 * 50 = 7500.0
    FoodProduct("Сыр", 450.0, "20.07.2026"),
    Phone("iPhone 15", 90000.0, 6)
]

print("=== ВСЕ ТОВАРЫ ===")
for item in catalog:
    print(item)

print("\n" + "=" * 50 + "\n")

budget = 8000.0
print(f"=== ДОСТУПНОСТЬ ДЛЯ ПОКУПАТЕЛЯ С БЮДЖЕТОМ {budget} РУБ. ===")
for item in catalog:
    status = "Можно купить" if item.is_affordable(budget) else "Не хватает денег"
    print(f"- {item.name}: {status}")

print("\n" + "=" * 50 + "\n")

max_search_price = 10000.0
print(f"=== ПОИСК ТОВАРОВ С ЦЕНОЙ ДО {max_search_price} РУБ. ===")
found_items = search_by_max_price(catalog, max_search_price)

for item in found_items:
    print(item)
