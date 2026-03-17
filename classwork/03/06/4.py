import pytest


class Employee:
    """
    Employee class: represents a company employee and their data.

    :param last_name: Employee last name.
    :type last_name: str
    :param first_name: Employee first name.
    :type first_name: str
    :param job_title: Employee job title.
    :type job_title: str
    :param salary: Employee salary in rubles.
    :type salary: int or float
    """

    def __init__(self, last_name, first_name, job_title, salary):
        """Initialize the employee's base attributes."""
        self.last_name = last_name
        self.first_name = first_name
        self.job_title = job_title
        self.salary = salary
        self._experience = 0

    def experience_get(self):
        """
        Return the employee's current work experience.

        :return: Current work experience in years.
        :rtype: int
        """
        return self._experience

    def experience_set(self, value):
        """
        Set the employee's work experience with negative-value validation.

        :param value: Experience value to set.
        :type value: int
        :raises ValueError: If the experience value is negative.
        """
        if value < 0:
            raise ValueError("Experience cannot be negative!")
        self._experience = value

    def is_high_salary(self):
        """
        Check the employee salary level (threshold: 100,000 RUB).

        :return: A string describing the salary level.
        :rtype: str
        """
        if self.salary > 100000:
            return "Salary is high (more than 100,000 rubles)"
        return "Salary is standard (100,000 rubles or less)"

    def __str__(self):
        """
        Return a formatted string with employee information.

        :return: A readable string representation of the employee.
        :rtype: str
        """
        return (
            f"Employee: {self.last_name} {self.first_name}\n"
            f"Job title: {self.job_title}\n"
            f"Salary: {self.salary} RUB\n"
            f"Experience: {self.experience} years"
        )

    experience = property(
        fget=experience_get,
        fset=experience_set,
        doc="Property for safe access to work experience.",
    )


# --- pytest test block ---


@pytest.fixture
def default_employee():
    """
    pytest fixture.
    Creates and returns a default employee object before each test
    to avoid duplicating initialization code.
    """
    return Employee("Ivanov", "Ivan", "Developer", 120000)


help(Employee)


print("\n[CLASS DESCRIPTION]")
print(Employee.__doc__.strip())


print("\n[CONSTRUCTOR __init__]")
print(Employee.__init__.__doc__.strip())

print("\n[METHOD is_high_salary]")
print(Employee.is_high_salary.__doc__.strip())

print("\n[PROPERTY experience]")
print(Employee.experience.__doc__.strip())

print("\n[GETTER experience_get]")
print(Employee.experience_get.__doc__.strip())

print("\n[SETTER experience_set]")
print(Employee.experience_set.__doc__.strip())

print("\n[METHOD __str__]")
print(Employee.__str__.__doc__.strip())
print("\n=========================================")
