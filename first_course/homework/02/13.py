# ==================================================
# TASK 1
# ==================================================
# DESCRIPTION:
# Create a Car class that contains the following fields:
# - car brand
# - car color
# - maximum speed
#
# Create two objects of this class and print their data.
#
# SOLUTION:
# ==================================================


class Car:
    def __init__(self, brand, color, max_speed):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed


car1 = Car("BMW", "Black", 250)
car2 = Car("Audi", "White", 230)

print()
print("Task 1")
print()

print(car1.brand, car1.color, car1.max_speed)
print(car2.brand, car2.color, car2.max_speed)
print()

# ==================================================
# TASK 2
# ==================================================
# DESCRIPTION:
# Add dynamic attributes to Car class objects:
# - car weight
# - number of owners
#
# Print the new data.
#
# SOLUTION:
# ==================================================

car1.weight = 1800
car1.owners = 2

car2.weight = 1650
car2.owners = 1

print()
print("Task 2")
print()

print("Weight:", car1.weight, "Owners:", car1.owners)
print("Weight:", car2.weight, "Owners:", car2.owners)
print()


# ==================================================
# TASK 3
# ==================================================
# DESCRIPTION:
# Add methods to the Car class:
# - total weight calculation
# - comparison of two cars by weight
# - full information output
#
# Implement the methods.
#
# SOLUTION:
# ==================================================


class CarAdvanced:
    def __init__(self, brand, color, max_speed, weight, quantity):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed
        self.weight = weight
        self.quantity = quantity

    def total_weight(self):
        return self.weight * self.quantity

    def compare(self, other):
        if self.total_weight() > other.total_weight():
            return "The first car is heavier"
        if self.total_weight() < other.total_weight():
            return "The second car is heavier"
        return "The weight is the same"

    def info(self):
        print("Brand:", self.brand)
        print("Color:", self.color)
        print("Speed:", self.max_speed)
        print("Total weight:", self.total_weight())
        print()


car3 = CarAdvanced("BMW", "Black", 250, 1800, 2)
car4 = CarAdvanced("Audi", "White", 230, 1600, 1)

print()
print("Task 3")
print()

car3.info()
car4.info()
print(car3.compare(car4))
print()


# ==================================================
# TASK 4
# ==================================================
# DESCRIPTION:
# Create a Student class with the following fields:
# - name
# - age
# - course
# - average grade
#
# Create methods for:
# - displaying information
# - displaying the average grade
#
# SOLUTION:
# ==================================================


class Student:
    def __init__(self, name, age, course, grade):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade

    def show_grade(self):
        print("Average grade:", self.grade)

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Grade:", self.grade)
        print()


student = Student("Maxim", 19, 2, 4.5)

print()
print("Task 4")
print()

student.info()
student.show_grade()
print()


# ==================================================
# TASK 5
# ==================================================
# DESCRIPTION:
# Add methods to the Student class for:
# - changing the name
# - changing the age
# - changing the average grade
#
# Verify the methods.
#
# SOLUTION:
# ==================================================


class StudentAdvanced(Student):
    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = new_age

    def change_grade(self, new_grade):
        self.grade = new_grade


student2 = StudentAdvanced("Maxim", 19, 2, 4.5)

print()
print("Task 5")
print()

student2.change_name("Alex")
student2.change_age(20)
student2.change_grade(4.9)

student2.info()
print()


# ==================================================
# TASK 6
# ==================================================
# DESCRIPTION:
# Create a Calculator class that accepts a string
# such as: "6 - 7 + 4"
#
# Implement expression evaluation
# using + and - operations.
#
# SOLUTION:
# ==================================================


class Calculator:
    def calculate(self, text):
        parts = text.split()

        result = int(parts[0])

        index = 1
        while index < len(parts):
            operator = parts[index]
            number = int(parts[index + 1])

            if operator == "+":
                result += number
            elif operator == "-":
                result -= number

            index += 2

        return result


calc = Calculator()

example1 = "12 - 19 + 1"
example2 = "1 - 3 + 10"

print()
print("Task 6")
print()

print("Example:", example1)
print("Result:", calc.calculate(example1))
print()

print("Example:", example2)
print("Result:", calc.calculate(example2))
print()
