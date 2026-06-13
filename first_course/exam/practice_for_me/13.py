"""
Создайте родительский класс ТРАНСПОРТ (информация, базовая грузоподъемность).

Реализуйте дочерние классы:

АВТОМОБИЛЬ (наследует базовые параметры)
МОТОЦИКЛ (без коляски, жестко задает грузоподъемность=0)
ГРУЗОВИК (при наличии прицепа динамически увеличивает грузоподьмность x 2)

Организуйте коллекцию объектов и реализуйте функцию поиска транспортных средств по строго заданному диапазону
грузоподъемности.
"""


class Transport:
    def __init__(self, name: str, base_capacity: float):
        self.name = name
        self._base_capacity = base_capacity

    @property
    def capacity(self) -> float:
        return self._base_capacity

    def __str__(self):
        return f"{self.name} ({self.capacity})"


class Car(Transport):
    pass


class Motorcycle(Transport):
    def __init__(self, name: str):
        super().__init__(name, 0)


class Truck(Transport):
    def __init__(self, name: str, base_capacity: float, has_trailer: bool = False):
        super().__init__(name, base_capacity)
        self.has_trailer = has_trailer

    @property
    def capacity(self) -> float:
        if self.has_trailer:
            return self._base_capacity * 2
        return self._base_capacity


def find_vehicles_by_capacity(vehicles: list, min_cap: float, max_cap: float) -> list:
    return [v for v in vehicles if min_cap <= v.capacity <= max_cap]
