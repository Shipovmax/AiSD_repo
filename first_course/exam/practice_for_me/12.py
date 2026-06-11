"""
Создайте класс Студент (имя, фамилия, возраст, список оценок).

Реализуйте методы
добавления оценка,
вычисления среднего балла и
вывод информации.

Используйте магический метод __len__
для получения количества оценок студента.
"""


class Student:
    def __init__(
        self, name: str, second_name: str, age: int, list_of_assessment: list = None
    ):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.list_of_assessment = (
            list_of_assessment if list_of_assessment is not None else []
        )

    def add_assessment(self, value: int):
        self.list_of_assessment.append(value)

    def gpa_calculations(self) -> float:
        if not self.list_of_assessment:
            return 0.0
        return sum(self.list_of_assessment) / len(self.list_of_assessment)

    def __len__(self) -> int:
        return len(self.list_of_assessment)

    def __str__(self) -> str:
        return (
            f"Студент: {self.second_name} {self.name} | Возраст: {self.age} | "
            f"Оценки: {self.list_of_assessment} | Средний балл: {self.gpa_calculations():.2f}"
        )
