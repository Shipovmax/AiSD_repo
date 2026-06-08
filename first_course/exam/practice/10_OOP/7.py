'''
Создайте класс СТУДЕНТ с методами вывода информации и проверки соответствия условиям.

Реализуйте дочерние классы:

БАКАЛАВР (имя, фамилия, возраст, курс)
МАГИСТР (имя, фамилия, возраст, специализация)
АСПИРАНТ (имя, фамилия, возраст, тема диссертации)
'''


class Student:
    def __init__(self, name: str, second_name: str, age: int):
        self.name = name
        self.second_name = second_name
        self.age = age

    def __str__(self):
        return f"Студент: {self.second_name} {self.name}, Возраст: {self.age}"

    def is_adult(self) -> bool:
        return self.age >= 18


class Bachelor(Student):
    def __init__(self, name: str, second_name: str, age: int, course: int):
        super().__init__(name, second_name, age)
        self.course = course

    def __str__(self):
        return super().__str__() + f", Курс: {self.course}"


class Master(Student):
    def __init__(self, name: str, second_name: str, age: int, specialization: str):
        super().__init__(name, second_name, age)
        self.specialization = specialization

    def __str__(self):
        return super().__str__() + f", Специализация: {self.specialization}"


class Postgraduate(Student):
    def __init__(self, name: str, second_name: str, age: int, thesis_topic: str):
        super().__init__(name, second_name, age)
        self.thesis_topic = thesis_topic

    def __str__(self):
        return super().__str__() + f"\nТема диссертации: {self.thesis_topic}"


bachelor = Bachelor("Иван", "Иванов", 19, 2)
print(bachelor)
print(f"Совершеннолетний? {bachelor.is_adult()}")  # True

print("-" * 30)

aspirant = Postgraduate("Петр", "Сидоров", 24, "Разработка ИИ на Python")
print(aspirant)
