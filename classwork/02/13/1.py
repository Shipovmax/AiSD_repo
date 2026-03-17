class Student:
    def __init__(self, name, age, class_name, average_grade):
        self.name = name
        self.age = age
        self.class_name = class_name
        self.average_grade = average_grade

    def change_grade(self, new_grade):
        self.average_grade = new_grade

    def get_grade(self):
        return self.average_grade

    def get_data(self):
        return (self.name, self.age, self.class_name, self.average_grade)

    def __str__(self):
        return (
            f"name {self.name} age {self.age} "
            f"class {self.class_name} grade {self.average_grade}"
        )


student_1 = Student("Vasia", 12, "9B", 4.5)
student_2 = Student("Ivan", 14, "11A", 3.2)

print(student_1.__dict__)
student_1.change_grade(4.8)
print(student_1.get_grade())
print(student_1.get_data())
print(student_1)
