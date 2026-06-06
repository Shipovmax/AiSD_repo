"""
Создай класс Book с атрибутами title (название) и author (автор).

Реализуй метод __str__,
чтобы при вызове print(book) выводилась красивая строка:
"Название" автор: Автор.

Реализуй метод __repr__,
чтобы он возвращал строку, по которой можно воссоздать объект:
Book('Название', 'Автор').
"""


class Book:
    def __init__(self, title, author) -> None:
        self.title  = title
        self.author = author

    def __str__(self) -> str:
        return f'"{self.title}" автор: {self.author}'

    def __repr__(self) -> str:
        return f"Book({self.title!r}, {self.author!r})"


book_test = Book("Муму", "Пушкин")
print(book_test)
