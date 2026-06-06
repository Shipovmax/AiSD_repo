class Student:
    """Base STUDENT class."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_info(self):
        """Display information about the object."""
        return f"Student: {self.first_name} {self.last_name}, Age: {self.age}"

    def matches_conditions(self, **kwargs):
        """
        Universal method for checking whether an object matches conditions.

        Named arguments are passed, for example: age=20, course=3.
        """
        for key, value in kwargs.items():
            # getattr returns the attribute value or None if the attribute is missing.
            if getattr(self, key, None) != value:
                return False
        return True


class Bachelor(Student):
    """Derived BACHELOR class."""

    def __init__(self, first_name, last_name, age, course):
        super().__init__(first_name, last_name, age)
        self.course = course

    def display_info(self):
        return (
            f"[Bachelor] {self.first_name} {self.last_name}, "
            f"Age: {self.age}, Course: {self.course}"
        )


class Master(Student):
    """Derived MASTER class."""

    def __init__(self, first_name, last_name, age, specialization):
        super().__init__(first_name, last_name, age)
        self.specialization = specialization

    def display_info(self):
        return (
            f"[Master] {self.first_name} {self.last_name}, "
            f"Age: {self.age}, Specialization: {self.specialization}"
        )


class Postgraduate(Student):
    """Derived POSTGRADUATE class."""

    def __init__(self, first_name, last_name, age, thesis_topic):
        super().__init__(first_name, last_name, age)
        self.thesis_topic = thesis_topic

    def display_info(self):
        return (
            f"[Postgraduate] {self.first_name} {self.last_name}, "
            f"Age: {self.age}, Thesis topic: '{self.thesis_topic}'"
        )


students_db = [
    Bachelor("Ivan", "Ivanov", 20, 3),
    Bachelor("Anna", "Petrova", 19, 2),
    Bachelor("Maxim", "Sidorov", 20, 3),
    Master("Elena", "Smirnova", 23, "Software Engineering"),
    Master("Alexey", "Volkov", 24, "Data Analysis"),
    Postgraduate("Dmitry", "Sokolov", 26, "AI Model Optimization"),
    Postgraduate("Olga", "Morozova", 25, "Information Security"),
]

print("=== COMPLETE STUDENT DATABASE ===")
for student in students_db:
    print(student.display_info())
print("\n" + "=" * 30 + "\n")


def search_students(database, **conditions):
    """Helper function for printing search results."""
    print(f"--- Search results for conditions: {conditions} ---")
    found = False
    for student in database:
        if student.matches_conditions(**conditions):
            print(student.display_info())
            found = True
    if not found:
        print("No students matching the conditions were found.")
    print()


search_students(students_db, age=20)
search_students(students_db, course=3)
search_students(students_db, specialization="Software Engineering")
search_students(students_db, age=25, thesis_topic="Information Security")
