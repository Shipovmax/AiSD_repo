'''
Создайте класс Магазин (название, список товаров).
Каждый товар — объект класса Товар (название, цена, количество).

Реализуйте методы добавления, удаления товара и вычисления общей стоимости.
Используйте __len__ для количества товаров.
'''


class Product:
    def __init__(self, name: str, price: int, count: int):
        self.name = name
        self.price = price
        self.count = count

    def __str__(self):
        return f"{self.name} (Цена: {self.price} руб., Количество: {self.count} шт.)"


class Shop:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_name: str):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                return True
        return False

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.count
        return total

    def __len__(self):
        total_count = 0
        for product in self.products:
            total_count += product.count
        return total_count

    def __str__(self):
        info = f"Магазин: {self.name}\nСписок товаров:\n"
        if not self.products:
            info += "Магазин пуст"
        for product in self.products:
            info += f"- {product}\n"
        return info


shop = Shop("Пятёрочка")

prod1 = Product("Молоко", 90, 5)
prod2 = Product("Хлеб", 50, 10)
prod3 = Product("Шоколад", 120, 3)

shop.add_product(prod1)
shop.add_product(prod2)
shop.add_product(prod3)

print(shop)
print(f"Общее количество товаров в магазине: {len(shop)} шт.")
print(f"Общая стоимость всех товаров: {shop.get_total_value()} руб.\n")

shop.remove_product("Хлеб")

print("=== ПОСЛЕ УДАЛЕНИЯ ХЛЕБА ===")
print(shop)
print(f"Общее количество товаров в магазине: {len(shop)} шт.")
print(f"Общая стоимость всех товаров: {shop.get_total_value()} руб.")
