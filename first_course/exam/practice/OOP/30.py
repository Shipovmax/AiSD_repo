'''
Создайте класс ТОВАР (информация, соответствие возрасту).
Дочерние классы: ИГРУШКА, КНИГА, СПОРТИНВЕНТАРЬ.
Организуйте поиск по возрастному диапазону.
'''


class Product:
    def __init__(self, name: str, price: float, min_age: int, max_age: int):
        self.name = name
        self.price = price
        self.min_age = min_age
        self.max_age = max_age

    def matches_age(self, age: int) -> bool:
        return self.min_age <= age <= self.max_age

    def __str__(self):
        return f"Товар: {self.name} | Цена: {self.price} руб. | Возраст: {self.min_age}-{self.max_age} лет"


class Toy(Product):
    def __init__(self, name: str, price: float, min_age: int, max_age: int, material: str):
        super().__init__(name, price, min_age, max_age)
        self.material = material

    def __str__(self):
        return f"Игрушка: {self.name} ({self.material}) | Цена: {self.price} руб. | Возраст: {self.min_age}-{self.max_age} лет"


class Book(Product):
    def __init__(self, name: str, price: float, min_age: int, max_age: int, author: str):
        super().__init__(name, price, min_age, max_age)
        self.author = author

    def __str__(self):
        return f"Книга: '{self.name}' - {self.author} | Цена: {self.price} руб. | Возраст: {self.min_age}-{self.max_age} лет"


class SportsEquipment(Product):
    def __init__(self, name: str, price: float, min_age: int, max_age: int, sport_type: str):
        super().__init__(name, price, min_age, max_age)
        self.sport_type = sport_type

    def __str__(self):
        return f"Спортинвентарь: {self.name} ({self.sport_type}) | Цена: {self.price} руб. | Возраст: {self.min_age}-{self.max_age} лет"


def search_by_age_range(catalog: list[Product], target_min_age: int, target_max_age: int) -> list[Product]:
    results = []
    for item in catalog:
        if item.min_age >= target_min_age and item.max_age <= target_max_age:
            results.append(item)
    return results


catalog = [
    Toy("Конструктор LEGO", 3500.0, 6, 12, "Пластик"),
    Book("Сказки Пушкина", 450.0, 3, 7, "А.С. Пушкин"),
    SportsEquipment("Футбольный мяч", 1200.0, 7, 99, "Футбол"),
    Toy("Погремушка", 150.0, 0, 2, "Текстиль"),
    Book("Энциклопедия для подростков", 800.0, 12, 17, "Коллектив авторов")
]

print("=== ВСЕ ТОВАРЫ ===")
