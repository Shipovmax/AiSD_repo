from datetime import datetime


class Company:
    """Class representing a construction company."""

    def __init__(self, name):
        self.name = name
        self.employees = []  # List of company employees.

    def add_employee(self, worker):
        """Add a worker to the company staff and link the worker to this company."""
        self.employees.append(worker)
        worker.company = self

    def __str__(self):
        return f"Company '{self.name}' (employees: {len(self.employees)})"


class Worker:
    """Class describing a worker."""

    def __init__(self, name, qualification, company=None):
        self.name = name
        self.qualification = qualification
        self.company = company
        # If a company is provided during creation, register the worker automatically.
        if company:
            company.add_employee(self)

    def __str__(self):
        # If no company is assigned, display 'Self-employed'.
        company_name = self.company.name if self.company else "Self-employed"
        return f"{self.name} ({self.qualification}) - {company_name}"


class House:
    """Class describing a construction object (house)."""

    def __init__(
        self,
        address,
        floors,
        entrances,
        district,
        workers,
        start_date_str,
        end_date_str,
    ):
        self.address = address
        self.floors = floors
        self.entrances = entrances
        self.district = district
        self.workers = workers  # Workers assigned to the object.

        # Convert date strings to datetime objects for convenient comparison.
        self.start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
        self.end_date = datetime.strptime(end_date_str, "%d.%m.%Y")

    def is_worker_busy_in_year(self, worker, year):
        """Check whether a specific worker was assigned to this object in the given year."""
        # 1. Check whether the worker is assigned to this house at all.
        if worker not in self.workers:
            return False

        # 2. Determine the boundaries of the requested year.
        year_start = datetime(year, 1, 1)
        year_end = datetime(year, 12, 31)

        # 3. Interval overlap logic.
        return self.start_date <= year_end and self.end_date >= year_start

    def __str__(self):
        return (
            f"Object in {self.district} district "
            f"({self.address}, {self.floors} floors, {self.entrances} entrances)"
        )


class Registry:
    """Registry class for storing all data and generating reports."""

    def __init__(self):
        self.houses = []
        self.workers = []

    def add_house(self, house):
        self.houses.append(house)

    def add_worker(self, worker):
        self.workers.append(worker)

    def show_worker_statistics(self, year):
        """Generate and print a report on worker workload for a specific year."""
        print(f"\n--- Worker workload report for {year} ---")
        for worker in self.workers:
            # Find all houses where this worker was assigned in the specified year.
            projects = [
                house
                for house in self.houses
                if house.is_worker_busy_in_year(worker, year)
            ]
            count = len(projects)

            if count > 0:
                print(f" {worker.name}: involved in {count} projects simultaneously.")
                for project in projects:
                    print(f"   - {project}")
            else:
                print(f" {worker.name}: there were no projects in this year.")


# --- Main program block ---
if __name__ == "__main__":
    # Create companies.
    stroy = Company("StroyGroup")
    mega = Company("MegaHouse")

    # Create workers and attach them to companies.
    worker_1 = Worker("Ivanov", "Foreman", stroy)
    worker_2 = Worker("Petrov", "Painter", stroy)
    worker_3 = Worker("Sidorov", "Electrician", mega)

    # Initialize the registry and populate it with data.
    registry = Registry()
    registry.add_worker(worker_1)
    registry.add_worker(worker_2)
    registry.add_worker(worker_3)

    # Add construction objects with different schedules.
    registry.add_house(
        House(
            "10 Lenin St.",
            5,
            4,
            "Central",
            [worker_1, worker_2],
            "01.01.2022",
            "31.12.2022",
        )
    )
    registry.add_house(
        House(
            "5 Mira Ave.",
            9,
            2,
            "Western",
            [worker_1, worker_3],
            "01.06.2022",
            "01.06.2023",
        )
    )
    registry.add_house(
        House(
            "2 Severnaya St.", 16, 1, "Northern", [worker_1], "01.01.2023", "01.12.2023"
        )
    )

    # Interactive section: request a year from the user.
    try:
        user_year = int(
            input("Enter a year to check statistics for (for example, 2022): ")
        )
        registry.show_worker_statistics(user_year)
    except ValueError:
        print("Error: please enter a numeric year value.")
