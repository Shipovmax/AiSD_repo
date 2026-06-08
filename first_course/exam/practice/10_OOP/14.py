'''
Создайте класс Студент (имя, фамилия, возраст, список оценок).
Реализуйте методы добавления оценки, вычисления среднего балла и вывод информации.
Используйте __len__ для количества оценок.
'''


class Student:
    def __init__(self, name: str, second_name: str, age: int):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.grades = []

    def add_grade(self, grade: int):
        if 1 <= grade <= 5:
            self.grades.append(grade)
            return True
        return False

    def get_average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __len__(self):
        return len(self.grades)

    def __str__(self):
        grades_str = ", ".join(map(str, self.grades)) if self.grades else "Нет оценок"
        return (f"Студент: {self.second_name} {self.name}\n"
                f"Возраст: {self.age} лет\n"
                f"Оценки: [{grades_str}]\n"
                f"Средний балл: {self.get_average_grade():.2f}\n"
                f"Количество оценок: {len(self)}\n"
                f"{'-' * 30}")


student = Student("Алексей", "Петров", 20)

student.add_grade(5)
student.add_grade(4)
student.add_grade(5)
student.add_grade(3)

print(student)
