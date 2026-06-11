"""
Опишите класс Product, заданный названием, ценой и количеством.

Включите в описание класса методы:
вывода информации о товаре на экран,
проверки, есть ли товар в наличии (количество больше 0),
и свойство, позволяющее установить категорию товара.
"""


class Product:
    def __init__(self, name: str, price: int, count: int):
        self.name = name
        self.price = price
        self.count = count
        self._category = ""

    def __str__(self) -> str:
        return f"Товар: {self.name} | Цена: {self.price} руб. | Количество: {self.count} шт."

    def is_available(self) -> bool:
        return self.count > 0

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value: str):
        self._category = value
