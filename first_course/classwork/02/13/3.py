"""Create Teacher and Student classes.

Based on the output of these classes, display all students taught by the
teacher. For each student, display information about the subject studied and
the resulting grade.
"""


class Student:
    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade

    def get_info(self):
        return f"Student: {self.name}, subject: {self.subject}, grade: {self.grade}"


class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []

    def teach(self, student):
        """Add a student taught by this teacher."""
        self.students.append(student)

    def show_students(self):
        print(f"Teacher {self.name} taught the following students:\n")

        if not self.students:
            print("There are no trained students.")
            return

        for student in self.students:
            print(student.get_info())


# Tests
print(" ")

teacher = Teacher("Ivan Petrov")

s1 = Student("Alexey", "Mathematics", 5)
s2 = Student("Maria", "Physics", 4)
s3 = Student("Dmitry", "Computer Science", 5)

teacher.teach(s1)
teacher.teach(s2)
teacher.teach(s3)

teacher.show_students()
print(" ")
