'''
Создайте родительский класс Сотрудник магазина (имя, зарплата, стаж)
и дочерние классы Кассир и Мерчендайзер.
'''


class Employee:
    def __init__(self, name: str, salary: int, experience: float):
        self.name = name
        self.salary = salary
        self.experience = experience

    def __str__(self):
        return (f"Сотрудник: {self.name}\n"
                f"Зарплата: {self.salary} руб.\n"
                f"Стаж: {self.experience} года/лет")


class Cashier(Employee):
    def __init__(self, name: str, salary: int, experience: float, till_number: int):
        super().__init__(name, salary, experience)
        self.till_number = till_number

    def __str__(self):
        return super().__str__() + f"\nНомер кассы: {self.till_number}\n{'-' * 30}"


class Merchandiser(Employee):
    def __init__(self, name: str, salary: int, experience: float, department: str):
        super().__init__(name, salary, experience)
        self.department = department

    def __str__(self):
        return super().__str__() + f"\nОтдел: {self.department}\n{'-' * 30}"


cashier = Cashier("Анна", 45000, 1.5, 3)
merchandiser = Merchandiser("Игорь", 40000, 0.5, "Бакалея")

print(cashier)
print(merchandiser)
