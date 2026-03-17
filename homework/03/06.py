class Employee:
    vacation_days = 28

    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f"Remaining vacation days: {self.remaining_vacation_days}."


class FullTimeEmployee(Employee):
    def get_unpaid_vacation(self, start_date, days):
        return (
            f"Unpaid vacation start date: {start_date}, "
            f"duration: {days} days."
        )


class PartTimeEmployee(Employee):
    # Override the number of days only for this class.
    vacation_days = 14


# --- Usage example ---

full_time = FullTimeEmployee("Robert", "Crusoe", "m")
print(f"Full-time ({full_time.first_name}): {full_time.get_vacation_details()}")
print(full_time.get_unpaid_vacation("2023-07-01", 5))

print("-" * 30)

part_time = PartTimeEmployee("Alena", "Pyatnitskaya", "f")
print(f"Part-time ({part_time.first_name}): {part_time.get_vacation_details()}")
