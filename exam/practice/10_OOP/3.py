'''
Опишите класс Employee,
заданный фамилией, именем, должностью и зарплатой.

Включите в описание класса методы:
вывода информации о сотруднике на экран,
проверки, является ли зарплата высокой (больше 100 000 рублей),
и свойство, позволяющее установить стаж работы.
'''


class Employee:
    def __init__(self, first_name: str, last_name: str, position: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary
        self._experience = None

    def __str__(self) -> str:
        return f"Сотрудник: {self.last_name} {self.first_name}, Должность: {self.position}, Зарплата: {self.salary} руб."

    def is_high_salary(self) -> bool:
        if self.salary < 0:
            print("Предупреждение: Зарплата не может быть отрицательной!")
            return False
        return self.salary > 100000

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value: int):
        if value < 0:
            print("Ошибка: Стаж работы не может быть отрицательным!")
        else:
            self._experience = value


emp = Employee("Иван", "Петров", "Python-разработчик", 120000)
print(emp)

if emp.is_high_salary():
    print("У этого сотрудника высокая зарплата.")
else:
    print("У этого сотрудника обычная зарплата.")

emp.experience = 3
print(f"Стаж работы: {emp.experience} года/лет")
