"""
Создайте односвязный список для хранения
и управления информацией о студентах в университете.

Каждый элемент списка должен содержать имя, фамилию,
номер студенческого билета и список курсов, на которые студент записан.
"""


class Student:
    """Узел списка, представляющий студента."""

    def __init__(self, first_name, last_name, student_id, courses=None):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.courses = courses if courses else []
        self.next = None  # Ссылка на следующего студента

    def __str__(self):
        return f"[{self.student_id}] {self.first_name} {self.last_name} | Курсы: {', '.join(self.courses)}"


class UniversityList:
    """Управляющий класс для односвязного списка."""

    def __init__(self):
        self.head = None

    def add_student(self, first_name, last_name, student_id, courses):
        """Добавление нового студента в начало списка."""
        new_student = Student(first_name, last_name, student_id, courses)
        new_student.next = self.head
        self.head = new_student
        print(f"Студент {last_name} успешно добавлен.")

    def find_by_id(self, student_id):
        """Поиск студента по номеру билета."""
        current = self.head
        while current:
            if current.student_id == student_id:
                return current
            current = current.next
        return None

    def display_all(self):
        """Вывод всех студентов в списке."""
        if not self.head:
            print("Список студентов пуст.")
            return

        print("\n--- Список студентов университета ---")
        current = self.head
        while current:
            print(current)
            current = current.next
        print("--------------------------------------\n")
