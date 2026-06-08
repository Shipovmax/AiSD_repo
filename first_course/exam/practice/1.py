'''
Опишите класс Book, заданный названием, автором, издательством и годом издания.

Включите в описание класса методы: вывода информации о книге на экран, проверки,
является ли книга новой (изданной в последние 5 лет), и свойство, позволяющее установить жанр книги.
'''

from datetime import datetime


class Book:
    def __init__(self, name: str, author: str, publisher: str, year_released: int) -> None:
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year_released = year_released
        self._genre = None

    def __str__(self) -> str:
        return (f"Книга: '{self.name}', Автор: {self.author}, "
                f"Издательство: {self.publisher}, Год: {self.year_released}")

    def check_if_new_book(self) -> bool:
        current_year = datetime.now().year
        if (current_year - self.year_released <= 5) == True:
            return f'Да'
        else:
            return f"Нет"

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value: str):
        self._genre = value


book = Book("Изучаем Python", "Марк Лутц", "О'Рейлли", 2024)

print(book)

print(f"Новая книга? {book.check_if_new_book()}")

book.genre = "Программирование"  # Установка работает как с обычной переменной
print(f"Жанр книги: {book.genre}")
