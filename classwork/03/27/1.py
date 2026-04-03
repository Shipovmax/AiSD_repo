"""
Шипов Максим Кириллович

Вариант 2
Задание 1


Создать класс Plane (самолетов), имеющий атрибуты: название самолета, количество пассажиров
на борту, курс движения (откуда и куда). Методы: - определить загрузку самолета, если максимальное
вместимость =200 пассажиров; - определить все имена самолетов, летящих по одному маршруту; - определить среднюю загрузку всех самолетов.

"""


class Plane:
    all_planes = []

    def __init__(self, name: str, passengers: int, from_city: str, to_city: str):
        self.name = name
        self.passengers = passengers
        self.from_city = from_city
        self.to_city = to_city
        Plane.all_planes.append(self)

    def get_load_percentage(self) -> float:
        max_capacity = 200
        return (self.passengers / max_capacity) * 100

    @classmethod
    def get_planes_by_route(cls, from_city: str, to_city: str) -> list[str]:
        return [
            plane.name
            for plane in cls.all_planes
            if plane.from_city == from_city and plane.to_city == to_city
        ]

    @classmethod
    def get_average_load(cls) -> float:
        if not cls.all_planes:
            return 0.0
        return sum(plane.get_load_percentage() for plane in cls.all_planes) / len(
            cls.all_planes
        )


if __name__ == "__main__":
    p1 = Plane("Boeing 737", 150, "Москва", "Санкт-Петербург")
    p2 = Plane("Airbus A320", 180, "Москва", "Санкт-Петербург")
    p3 = Plane("Boeing 777", 120, "Москва", "Казань")

    print(f"Загрузка {p1.name}: {p1.get_load_percentage():.1f}%")
    print(f"Загрузка {p2.name}: {p2.get_load_percentage():.1f}%")
    print(f"Загрузка {p3.name}: {p3.get_load_percentage():.1f}%")

    print(f"\nСамолеты на маршруте Москва -> Санкт-Петербург:")
    print(Plane.get_planes_by_route("Москва", "Санкт-Петербург"))

    print(f"\nСредняя загрузка всех самолетов: {Plane.get_average_load():.1f}%")
