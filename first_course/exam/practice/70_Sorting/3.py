"""
Реализуйте сортировку списка пользователей по возрасту методом выбора.
"""


class User:
    """Класс для представления пользователя."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age} лет)"

    @classmethod
    def selection_sort_by_age(cls, users):
        """
        Сортирует список пользователей по возрасту методом выбора (in-place).

        :param users: список объектов User
        """
        n = len(users)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if users[j].age < users[min_index].age:
                    min_index = j
            if min_index != i:
                users[i], users[min_index] = users[min_index], users[i]


if __name__ == "__main__":
    users = [
        User("Анна", 25),
        User("Иван", 30),
        User("Мария", 22),
        User("Петр", 28),
        User("Елена", 19),
    ]

    print("До сортировки:")
    print(users)

    User.selection_sort_by_age(users)

    print("\nПосле сортировки по возрасту (метод выбора):")
    print(users)
