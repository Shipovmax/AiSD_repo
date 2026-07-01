'''
Создайте класс Book (автор, название, год, цена). Найдите самую дорогую книгу, используя магические методы сравнения.
'''


class Book:
    def __init__(self, author: str, title: str, year: int, price: float):
        self.author = author
        self.title = title
        self.year = year
        self.price = price

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.price < other.price
        return NotImplemented

    def __str__(self):
        return f"'{self.title}' - {self.author} ({self.year} г.), цена: {self.price} руб."


books = [
    Book("Михаил Булгаков", "Мастер и Маргарита", 1967, 850.0),
    Book("Фёдор Достоевский", "Преступление и наказание", 1866, 620.0),
    Book("Джордж Оруэлл", "1984", 1949, 1200.0),
    Book("Лев Толстой", "Война и мир", 1869, 1100.0)
]

most_expensive_book = max(books)

print("=== СПИСОК КНИГ ===")
for book in books:
    print(book)

print("\n=== САМАЯ ДОРОГАЯ КНИГА ===")
print(most_expensive_book)
