'''
Создайте класс Person (информация, определение возраста).
Реализуйте дочерние классы: АБИТУРИЕНТ, СТУДЕНТ, ПРЕПОДАВАТЕЛЬ.
Организуйте поиск персон в заданном возрастном диапазоне.
'''

from datetime import datetime


class Person:
    def __init__(self, name: str, surname: str, birth_year: int):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def get_age(self) -> int:
        current_year = datetime.now().year
        return current_year - self.birth_year

    def __str__(self):
        return f"{self.surname} {self.name}, Возраст: {self.get_age()} лет"


class Enrollee(Person):
    def __init__(self, name: str, surname: str, birth_year: int, faculty: str):
        super().__init__(name, surname, birth_year)
        self.faculty = faculty

    def __str__(self):
        return f"Абитуриент: {super().__str__()}, Факультет: {self.faculty}"


class Student(Person):
    def __init__(self, name: str, surname: str, birth_year: int, course: int):
        super().__init__(name, surname, birth_year)
        self.course = course

    def __str__(self):
        return f"Студент: {super().__str__()}, Курс: {self.course}"


class Teacher(Person):
    def __init__(self, name: str, surname: str, birth_year: int, department: str):
        super().__init__(name, surname, birth_year)
        self.department = department

    def __str__(self):
        return f"Преподаватель: {super().__str__()}, Кафедра: {self.department}"


def search_by_age_range(people_list: list[Person], min_age: int, max_age: int) -> list[Person]:
    results = []
    for person in people_list:
        if min_age <= person.get_age() <= max_age:
            results.append(person)
    return results


database = [
    Enrollee("Иван", "Петров", 2009, "ИВТ"),
    Student("Анна", "Сидорова", 2006, 2),
    Teacher("Сергей", "Иванов", 1981, "Высшая математика"),
    Student("Елена", "Козлова", 2004, 4),
    Teacher("Ольга", "Смирнова", 1993, "Программирование")
]

print("=== ВСЯ БАЗА ПЕРСОН ===")
for p in database:
    print(p)

print("\n" + "=" * 50 + "\n")

min_a, max_a = 20, 35
print(f"=== ПОИСК ПЕРСОН В ДИАПАЗОНЕ ОТ {min_a} ДО {max_a} ЛЕТ ===")
found_people = search_by_age_range(database, min_a, max_a)

if found_people:
    for p in found_people:
        print(p)
else:
    print("Никто не найден")
