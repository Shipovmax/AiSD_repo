'''
Создайте классы Дом (этажность, подъезды, район, список рабочих) и
Рабочие (компания, квалификация).

Определите, в скольких постройках рабочий задействован в один год (формат даты 01.01.2022).
'''

from datetime import datetime


class Workers:
    def __init__(self, company: str, qualification: str):
        self.company = company
        self.qualification = qualification


class Home:
    def __init__(self, floors: int, entrances: int, district: str, start_date: str):
        self.floors = floors
        self.entrances = entrances
        self.district = district
        self.start_date = datetime.strptime(start_date, "%d.%m.%Y")
        self.workers = []

    def add_worker(self, worker: Workers):
        self.workers.append(worker)


def count_buildings_by_worker_and_year(building_list: list[Home], worker: Workers, year: int) -> int:
    count = 0
    for home in building_list:
        if home.start_date.year == year and worker in home.workers:
            count += 1
    return count


worker1 = Workers("СтройИнвест", "Маляр")
worker2 = Workers("ПрофРемонт", "Прораб")

home1 = Home(9, 3, "Центральный", "15.03.2022")
home2 = Home(16, 2, "Северный", "01.07.2022")
home3 = Home(5, 4, "Западный", "10.11.2023")

home1.add_worker(worker1)
home1.add_worker(worker2)

home2.add_worker(worker1)

home3.add_worker(worker1)

all_buildings = [home1, home2, home3]

buildings_in_2022 = count_buildings_by_worker_and_year(all_buildings, worker1, 2022)
buildings_in_2023 = count_buildings_by_worker_and_year(all_buildings, worker1, 2023)

print(f"Рабочий1 задействован в 2022 году в постройках: {buildings_in_2022}")
print(f"Рабочий1 задействован в 2023 году в постройках: {buildings_in_2023}")
