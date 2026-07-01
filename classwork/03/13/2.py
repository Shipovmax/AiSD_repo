class Employee:
    vacation_days = 28

    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days
        self._employee_id = self.__generate_employee_id()

    def __generate_employee_id(self):
        return hash(self.first_name + self.last_name + self.gender)

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f"Remaining vacation days: {self.remaining_vacation_days}."


class FullTimeEmployee(Employee):
    def __init__(self, first_name, last_name, gender, salary):
        super().__init__(first_name, last_name, gender)
        self.__salary = salary

    def __get_vacation_salary(self):
        return self.__salary * 0.8

    def get_unpaid_vacation(self, start_date, days):
        return f"Unpaid vacation start date: {start_date}, duration: {days} days."

    def get_vacation_salary_info(self):
        return f"Vacation pay amount: {self.__get_vacation_salary()}"


class PartTimeEmployee(Employee):
    pass


# Usage example:

full_time_employee = FullTimeEmployee("Ivan", "Ivanov", "m", 50000)
print(f"Employee ID: {full_time_employee._employee_id}")
print(full_time_employee.get_unpaid_vacation("2023-07-01", 5))
print(full_time_employee.get_vacation_salary_info())

part_time_employee = PartTimeEmployee("Anna", "Petrova", "f")
part_time_employee.consume_vacation(5)
print(f"Employee ID: {part_time_employee._employee_id}")
print(part_time_employee.get_vacation_details())
