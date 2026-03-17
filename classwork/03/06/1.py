class Employee:
    def __init__(self, last_name, first_name, job_title, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.job_title = job_title  # Job title
        self.salary = salary
        self._experience = 0  # Work experience

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value < 0:
            print("Experience cannot be negative!")
        else:
            self._experience = value

    def is_high_salary(self):
        if self.salary > 100000:
            return "Salary is high (more than 100,000 rubles)"
        return "Salary is standard (100,000 rubles or less)"

    def __str__(self):
        return (
            f"Employee: {self.last_name} {self.first_name}\n"
            f"Job title: {self.job_title}\n"
            f"Salary: {self.salary} RUB\n"
            f"Experience: {self.experience} years"
        )


employee = Employee("Ivanov", "Ivan", "Developer", 120000)
employee.experience = 5
print(employee)
print(employee.is_high_salary())
