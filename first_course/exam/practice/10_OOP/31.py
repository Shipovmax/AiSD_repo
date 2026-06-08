'''
Создайте класс ТЕЛЕФОННЫЙ_СПРАВОЧНИК (информация, поиск записи).
Дочерние классы: ПЕРСОНА, ОРГАНИЗАЦИЯ, ДРУГ. Организуйте поиск по фамилии.
'''


class PhoneDirectory:
    def __init__(self, phone: str):
        self.phone = phone

    def match_surname(self, surname: str) -> bool:
        return False

    def __str__(self):
        return f"Телефон: {self.phone}"


class Person(PhoneDirectory):
    def __init__(self, surname: str, name: str, phone: str):
        super().__init__(phone)
        self.surname = surname
        self.name = name

    def match_surname(self, surname: str) -> bool:
        return self.surname.lower() == surname.lower()

    def __str__(self):
        return f"Абонент: {self.surname} {self.name} | {super().__str__()}"


class Organization(PhoneDirectory):
    def __init__(self, title: str, contact_person_surname: str, phone: str, fax: str):
        super().__init__(phone)
        self.title = title
        self.contact_person_surname = contact_person_surname
        self.fax = fax

    def match_surname(self, surname: str) -> bool:
        return self.contact_person_surname.lower() == surname.lower()

    def __str__(self):
        return f"Организация: '{self.title}' (Контактное лицо: {self.contact_person_surname}) | {super().__str__()} | Факс: {self.fax}"


class Friend(PhoneDirectory):
    def __init__(self, surname: str, name: str, phone: str, birth_date: str):
        super().__init__(phone)
        self.surname = surname
        self.name = name
        self.birth_date = birth_date

    def match_surname(self, surname: str) -> bool:
        return self.surname.lower() == surname.lower()

    def __str__(self):
        return f"Друг: {self.surname} {self.name} | {super().__str__()} | ДР: {self.birth_date}"


def search_by_surname(directory: list[PhoneDirectory], surname: str) -> list[PhoneDirectory]:
    return [entry for entry in directory if entry.match_surname(surname)]


directory = [
    Person("Петров", "Иван", "+7-999-111-22-33"),
    Organization("ТехноПром", "Иванов", "+7-495-555-44-55", "555-44-56"),
    Friend("Петров", "Алексей", "+7-911-333-44-55", "15.04.1998"),
    Person("Сидорова", "Елена", "+7-900-777-88-99"),
    Friend("Иванов", "Дмитрий", "+7-950-222-11-00", "01.12.1995")
]

print("=== ВЕСЬ СПРАВОЧНИК ===")
for entry in directory:
    print(entry)

print("\n" + "=" * 60 + "\n")

search_surname = "Петров"
print(f"=== ПОИСК ЗАПИСЕЙ ПО ФАМИЛИИ '{search_surname}' ===")
results = search_by_surname(directory, search_surname)

if results:
    for entry in results:
        print(entry)
else:
    print("Записи не найдены")
