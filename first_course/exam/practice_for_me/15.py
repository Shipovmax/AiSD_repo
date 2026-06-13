"""
Создайте класс Дом (этажность, подъезды, район, список работающих на объекте сотрудников)
и класс Рабочие (компания, квалификация).

Каждый рабочий может быть закреплен за объектом в определенный промежуток времени.

Напишите метод, принимающий на вход конкретного рабочего и целевой год (формат даты 01.01.2022),
который определяет, в скольких постройках данный рабочий был задействован в течение этого года.
"""

from datetime import datetime


class Worker:
    def __init__(self, company: str, qualification: str):
        self.company = company
        self.qualification = qualification


class House:
    def __init__(self, floors: int, entrances: int, district: str):
        self.floors = floors
        self.entrances = entrances
        self.district = district
        self.schedule = []

    def assign_worker(self, worker: Worker, start_date_str: str, end_date_str: str):
        start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
        end_date = datetime.strptime(end_date_str, "%d.%m.%Y")
        if start_date > end_date:
            raise ValueError("Дата начала не может быть позже даты окончания")
        self.schedule.append((worker, start_date, end_date))

    def is_worker_active_in_year(self, worker: Worker, year_date_str: str) -> bool:
        target_year = datetime.strptime(year_date_str, "%d.%m.%Y").year
        year_start = datetime(target_year, 1, 1)
        year_end = datetime(target_year, 12, 31)

        for assigned_worker, start, end in self.schedule:
            if assigned_worker == worker:
                if not (end < year_start or start > year_end):
                    return True
        return False


def count_worker_objects_by_year(
    houses: list[House], worker: Worker, year_date_str: str
) -> int:
    count = 0
    for house in houses:
        if house.is_worker_active_in_year(worker, year_date_str):
            count += 1
    return count
