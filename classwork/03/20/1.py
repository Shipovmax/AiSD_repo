class LibraryItem:
    """Базовый класс, представляющий любой библиотечный элемент."""

    def __init__(self, title: str, item_id: str, pages: int):
        self.title = title
        self.item_id = item_id
        self.pages = pages

    def describe(self) -> str:
        """Возвращает базовое описание элемента."""
        return f"Издание '{self.title}' с ID {self.item_id}"

    def __str__(self) -> str:
        return f"{self.title} (ID: {self.item_id}), страниц: {self.pages}"

    def __eq__(self, other) -> bool:
        """Сравнивает элементы по количеству страниц. =="""
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return self.pages == other.pages

    def __lt__(self, other) -> bool:
        """Сравнивает элементы по количеству страниц. <"""
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return self.pages < other.pages


class Book(LibraryItem):
    """Класс, представляющий книгу, наследующийся от LibraryItem."""

    def __init__(self, title: str, item_id: str, pages: int, author: str):
        super().__init__(title, item_id, pages)
        self.author = author

    def describe(self) -> str:
        return f"Книга '{self.title}' от автора {self.author}"

    def __str__(self) -> str:
        return (
            f"{self.title} от {self.author} (ID: {self.item_id}), страниц: {self.pages}"
        )

    def __add__(self, other):
        """Складывает две книги, если они имеют одного автора."""

        if not isinstance(other, Book):
            raise ValueError("Можно добавить книгу только к другой книге.")
        if self.author != other.author:
            raise ValueError("Книги должны иметь одного автора для объединения.")

        new_title = f"{self.title} и {other.title}"
        return Book(new_title, "None", self.pages + other.pages, self.author)


class Magazine(LibraryItem):
    """Класс, представляющий журнал, наследующийся от LibraryItem."""

    def __init__(self, title: str, item_id: str, pages: int, issue_number: int):
        super().__init__(title, item_id, pages)
        self.issue_number = issue_number

    def describe(self) -> str:
        return f"Журнал '{self.title}', выпуск {self.issue_number}"

    def __str__(self) -> str:
        return f"{self.title}, выпуск {self.issue_number} (ID: {self.item_id}), страниц: {self.pages}"

    def __gt__(self, other) -> bool:
        """Сравнивает элементы по номеру выпуска. >"""
        if not isinstance(other, Magazine):
            return NotImplemented
        return self.issue_number > other.issue_number


if __name__ == "__main__":
    # Сценарий тестирования
    book1 = Book("Война и мир", "B001", 1200, "Л. Толстой")
    mag1 = Magazine("Наука", "M001", 50, 15)

    # Вывод строковых представлений
    print(book1)
    print(mag1)

    # Выполнение сравнений
    print(f"book1 == mag1: {book1 == mag1}")
    print(f"book1 < mag1: {book1 < mag1}")

    # Объединение книг
    book2 = Book("Анна Каренина", "B002", 800, "Л. Толстой")
    book3 = book1 + book2
    print(book3)

    # Сравнение журналов
    mag2 = Magazine("Природа", "M002", 60, 10)
    print(f"mag1 > mag2: {mag1 > mag2}")
