'''
Создайте класс СПОРТСМЕН с методами вывода информации и проверки соответствия условиям.

Реализуйте дочерние классы:

ЛЕГКОАТЛЕТ (имя, фамилия, возраст, дисциплина)
ПЛОВЕЦ (имя, фамилия, возраст, дистанция)
БОКСЕР (имя, фамилия, возраст, весовая категория)

Дополнительно: Создайте список спортсменов, выведите всю базу и организуйте поиск по имени или возрасту.
'''


class Sportsman:
    def __init__(self, name: str, second_name: str, age: int, sport_type: str):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.sport_type = sport_type

    def __str__(self):
        return (f"Спортсмен  -> {self.second_name} {self.name}\n"
                f"Возраст    -> {self.age} лет\n"
                f"Вид спорта -> {self.sport_type}")


class Athlete(Sportsman):
    def __init__(self, name: str, second_name: str, age: int, discipline: str):
        super().__init__(name, second_name, age, "Легкая атлетика")
        self.discipline = discipline

    def __str__(self):
        return super().__str__() + f"\nДисциплина -> {self.discipline}\n{'-' * 30}"


class Swimmer(Sportsman):
    def __init__(self, name: str, second_name: str, age: int, distance: int):
        super().__init__(name, second_name, age, "Плавание")
        self.distance = distance

    def __str__(self):
        return super().__str__() + f"\nДистанция  -> {self.distance} м\n{'-' * 30}"


class Boxer(Sportsman):
    def __init__(self, name: str, second_name: str, age: int, weight_category: str):
        super().__init__(name, second_name, age, "Бокс")
        self.weight_category = weight_category

    def __str__(self):
        return super().__str__() + f"\nВес. катег.-> {self.weight_category}\n{'-' * 30}"


def search_sportsmen(database, name: str = None, age: int = None):
    results = []
    for person in database:
        if name and person.name.lower() != name.lower():
            continue
        if age and person.age != age:
            continue
        results.append(person)
    return results


sportsmen_database = [
    Athlete("Иван", "Иванов", 20, "Бег 100м"),
    Swimmer("Анна", "Петрова", 18, 100),
    Boxer("Майк", "Тайсон", 25, "Тяжелый вес"),
    Athlete("Сергей", "Бубка", 22, "Прыжки с шестом"),
    Swimmer("Иван", "Сидоров", 25, 50)
]

print("=== ВСЯ БАЗА СПОРТСМЕНОВ ===")
for athlete in sportsmen_database:
    print(athlete)

print("\n" + "=" * 40 + "\n")

print("=== ПОИСК: По имени 'Иван' ===")
found_by_name = search_sportsmen(sportsmen_database, name="Иван")
for person in found_by_name:
    print(person)

print("=== ПОИСК: По возрасту '25 лет' ===")
found_by_age = search_sportsmen(sportsmen_database, age=25)
for person in found_by_age:
    print(person)
